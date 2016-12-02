#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulated Annealing
"""
import random

from ag_frame.algorithms import base
from ag_frame.algorithms import utils


class SA(base.Algorithm):
    """Simulated Annealing."""

    _name = "Simulated Annealing"

    def __init__(self):
        super(SA, self).__init__()
        self.size_var = []
        self.domains = None
        self.temperature = self._args.temperature
        self.step = self._args.step

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    @classmethod
    def add_parser(cls, base_parser, functions_list):
        """Add the apropiate subparser.

        :param base_parser: The Top-Level parser.
        :param functions_list: the list with functions.
        """
        super(SA, cls).add_parser(base_parser, functions_list)
        cls._parser.add_argument(
            "-t", "--temperature", type=float,
            help="The starting temperature [0, 1] (default 0.9)")
        cls._parser.add_argument(
            "-s", "--step", type=float,
            help="The step temperature (0, 1) (default 0.3)")
        cls._parser.set_defaults(temperature=.9, step=.3)

    def execute(self, function):
        """The algorithm implementation."""
        self.size_var = []
        self.domains = function.get_domain_restrictions

        for i in range(function.nr_args):
            size = utils.get_nr_bits(self.domains[i], self.precision)
            self.size_var.append(size)

        temperature = self.temperature
        big_string = '0' * sum(self.size_var)
        big_string = utils.randomise_a_string(big_string)

        global_best = big_string

        # NOTE(mmicu): Truncate the temperature to 4 decimal places
        while float("%.4f" % temperature) > 0:
            new = '0' * sum(self.size_var)
            new = utils.randomise_a_string(big_string)

            args_new = self.string_to_args(new)
            args_global_best = self.string_to_args(global_best)

            f_new = function(*args_new)
            f_global = function(*args_global_best)
            if f_new < f_global:
                global_best = new
            else:
                probability = random.random()
                if probability < ((f_global - f_new) / temperature) ** 2:
                    global_best = new
            temperature *= self.step

        return self.string_to_args(global_best)
