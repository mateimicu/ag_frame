#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Random Mutation Hill Climbing.
"""
from ag_frame.algorithms import base
from ag_frame.algorithms import utils


class RMHC(base.Algorithm):
    """Random Mutation Hill Climbing."""

    _name = "Random Mutation Hill Climbing"

    def __init__(self):
        super(RMHC, self).__init__()
        self.domains = None

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
        super(RMHC, cls).add_parser(base_parser, functions_list)
        cls._parser.add_argument(
            "-r", "--random_try", type=int,
            help="How many times we should try a random guess"
            " for a single run.")
        cls._parser.set_defaults(random_try=100)

    def execute(self, function):
        """The algorithm implementation."""
        self.domains = function.get_domain_restrictions

        self._prepare_size_var(function)

        big_string = '0' * sum(self.size_var)
        big_string = utils.randomise_a_string(big_string)

        best = big_string
        new = best
        retry = self._args.random_try
        while retry >= 0:
            new = utils.mutate_random(best)

            args_best = self.string_to_args(best)
            args_new = self.string_to_args(new)

            f_best = function.fit(*args_best)
            f_new = function.fit(*args_new)

            if f_new > f_best:
                best = new  # get a new best
                retry = self._args.random_try  # reset the retry
            else:
                retry -= 1
        return self.string_to_args(best)
