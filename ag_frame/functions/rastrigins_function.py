#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rastrigin's function is based on function 1 with the addition of cosine
modulation to produce many local minima. Thus, the
test function is highly multimodal.
However, the location of the minima are regularly distributed.
"""
import math

from ag_frame.functions import base


class RastriginsFunction(base.Function):
    """Rastrigin's function ."""

    _name = "Rastrigin's function"

    def __init__(self, **kwargs):
        """Initialize this function.

        :param dimensions: The number of dimension ( The default one is 6 )
        """
        dimensions = kwargs.get("dimension", self._args.dimensions)
        local_mins = (
            tuple([0 for _ in range(dimensions)]),
        )
        super(RastriginsFunction, self).__init__(
            nr_args=dimensions, default_domain=(-5.12, 5.12),
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
        super(RastriginsFunction, cls).add_parser(base_parser)
        cls.parser.set_defaults(dimensions=6)

    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        # f6(x)=10·n+sum(x(i)^2-10·cos(2·pi·x(i))), i=1:n; -5.12<=x(i)<=5.12.

        base_value = 10 * (self.nr_args)

        f_sum = 0
        for val in args:
            f_sum += (val**2 - 10*math.cos(2*math.pi*val))

        return base_value + f_sum
