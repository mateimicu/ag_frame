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

    def __init__(self, dimensions=6):
        """Initialize this function.

        :param dimensions: The number of dimension ( The default one is 6 )
        """
        local_mins = (
            tuple([0 for _ in range(dimensions)]),
        )
        super(RastriginsFunction, self).__init__(
            name="Rastrigin's function",
            nr_args=dimensions, default_domain=(-5.12, 5.12),
            local_mins=local_mins)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

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
