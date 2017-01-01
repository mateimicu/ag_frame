#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Mathematical functions.
"""
import math

from ag_frame.functions import base


class GriewangksFunction(base.Function):
    """Griewangk's function 8.

    Griewangk's function is similar to Rastrigin's function.
    It has many widespread local minima. However, the location of
    the minima are regularly distributed.
    """

    _name = "Griewangk's function"

    def __init__(self, **kwargs):
        """Initialize this function.

        :param dimensions: The number of dimension ( The default one is 8 )
        """
        dimensions = kwargs.get("dimension", self._args.dimensions)
        local_mins = (
            tuple([0 for _ in range(dimensions)]),
        )
        super(GriewangksFunction, self).__init__(
            nr_args=dimensions, default_domain=(-600, 600),
            local_mins=local_mins)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    @classmethod
    def add_parser(cls, base_parser):
        """Add the default parser for this function.

        :param parser: The top-level parser
        """
        super(GriewangksFunction, cls).add_parser(base_parser)
        cls.parser.set_defaults(dimensions=8)

    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        # f8(x) = sum(x(i)^2/4000)- prod(cos(x(i)/sqrt(i)))+1

        f_sum = 0
        f_prod = 1
        for index, val in enumerate(args):
            f_sum += (val ** 2) / 4000
            f_prod *= math.cos(val / math.sqrt(index+1))

        return f_sum - f_prod + 1
