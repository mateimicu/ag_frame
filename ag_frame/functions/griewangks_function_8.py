#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Mathematical functions.
"""
import math

from ag_frame.functions import base


class GriewangksFunction8(base.Function):
    """Griewangk's function 8.

    Griewangk's function is similar to Rastrigin's function.
    It has many widespread local minima. However, the location of
    the minima are regularly distributed.
    """

    def __init__(self):
        local_mins = (
            tuple([0 for _ in range(8)]),
        )
        super(GriewangksFunction8, self).__init__(
            name="Griewangk's function 8",
            nr_args=8, default_domain=(-600, 600),
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
        # f8(x) = sum(x(i)^2/4000)- prod(cos(x(i)/sqrt(i)))+1

        f_sum = 0
        f_prod = 1
        for index, val in enumerate(args):
            f_sum += (args[val] ** 2) / 4000
            f_prod *= math.cos(args[val] / math.sqrt(index+1))

        return f_sum - f_prod + 1
