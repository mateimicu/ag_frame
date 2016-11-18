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
        self.size_var = []
        self.domains = None
        self.precision = 300
        self.max_retry = 10000

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    def execute(self, function):
        """The algorithm implementation."""
        self.domains = function.get_domain_restrictions

        for index in range(function.nr_args):
            size = utils.get_nr_bits(self.domains[index], self.precision)
            self.size_var.append(size)

        big_string = '0' * sum(self.size_var)
        big_string = utils.randomise_a_string(big_string)

        best = big_string
        new = best
        retry = self.max_retry

        while retry >= 0:
            new = utils.mutate_random(best)

            args_best = self.string_to_args(best)
            args_new = self.string_to_args(new)

            f_best = function(*args_best)
            f_new = function(*args_new)

            if f_new < f_best:
                best = new  # get a new best
                retry = self.max_retry  # reset the retry
            else:
                retry -= 1
        return self.string_to_args(best)
