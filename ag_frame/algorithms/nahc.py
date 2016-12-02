#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Next Ascent Hill Climbing
"""
from ag_frame.algorithms import base
from ag_frame.algorithms import utils
TRY = True


class NAHC(base.Algorithm):
    """Next Ascent Hill Climbing."""

    _name = "Next Ascent Hill Climbing"

    def __init__(self):
        super(NAHC, self).__init__()
        self.size_var = []
        self.domains = None

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    def execute(self, function):
        """The algorithm implementation."""
        self.size_var = []
        self.domains = function.get_domain_restrictions

        for i in range(function.nr_args):
            size = utils.get_nr_bits(self.domains[i], self.precision)
            self.size_var.append(size)

        big_string = '0' * sum(self.size_var)
        big_string = utils.randomise_a_string(big_string)

        best = big_string
        new = best
        for index in range(len(big_string)):
            new = utils.mutate(best, index)

            args_best = self.string_to_args(best)
            args_new = self.string_to_args(new)

            f_best = function(*args_best)
            f_new = function(*args_new)

            if f_new < f_best:
                best = new

        return self.string_to_args(best)
