#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rosenbrock's valley is a classic optimization problem,
also known as Banana function. The global optimum is inside a
long, narrow, parabolic shaped flat valley. To find the valley is trivial,
however convergence to the global optimum is difficult and hence this
problem has been repeatedly used
in assess the performance of optimization algorithms.
"""
from ag_frame.functions import base


class GriewangksFunction8(base.Function):
    """Rosenbrock's valley (De Jong's function 2)."""

    def __init__(self):
        local_mins = (
            tuple([1, 1]),
        )
        super(GriewangksFunction8, self).__init__(
            name="Rosenbrock's valley",
            nr_args=2, default_domain=(-2.048, 2.048),
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
        # f2(x) = sum(100·(x(i+1)-x(i)^2)^2+(1-x(i))^2)
        return 100 * ((args[1] - args[0]**2)**2 + (1+args[0])**2)
