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


class RosenbrockValley(base.Function):
    """Rosenbrock's valley."""

    def __init__(self, dimensions=2):
        """Initialize this function.

        :param dimensions: The number of dimension ( The default one is 2 )
        """
        local_mins = (
            tuple([0 for _ in range(dimensions)]),
        )
        super(RosenbrockValley, self).__init__(
            name="Rosenbrock's valley",
            nr_args=dimensions, default_domain=(-2.048, 2.048),
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
        r_sum = 0
        for index in range(len(args)-1):
            r_sum += 100 * ((args[index+1] - args[index]**2)**2 +
                            (1+args[index])**2)
