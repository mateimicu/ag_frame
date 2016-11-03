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


class RastriginsFunction6(base.Function):
    """Rastrigin's function 6."""

    def __init__(self):
        local_mins = (
            tuple([0 for _ in range(6)]),
        )
        super(RastriginsFunction6, self).__init__(
            name="Rastrigin's function 6",
            nr_args=6, default_domain=(-5.12, 5.12),
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

        base_value = 10 * (self._nr_args + 1)

        f_sum = 0
        for index, val in enumerate(args):
            f_sum = (val**2 - 10*math.cos(2*math.pi*val))

        return base_value + f_sum
