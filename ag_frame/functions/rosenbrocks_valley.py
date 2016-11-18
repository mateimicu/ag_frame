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

    _name = "Rosenbrock's valley"

    def __init__(self):
        """Initialize this function."""
        local_mins = (
            tuple([0 for _ in range(self._args.dimensions)]),
        )
        super(RosenbrockValley, self).__init__(
            nr_args=self._args.dimensions, default_domain=(-2.048, 2.048),
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
        super(RosenbrockValley, cls).add_parser(base_parser)
        cls.parser.set_defaults(dimensions=2)

    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        # f2(x) = sum(100·(x(i+1)-x(i)^2)^2+(1-x(i))^2)
        r_sum = 0
        for index in range(len(args)-1):
            r_sum += 100 * ((args[index+1] - args[index]**2)**2 +
                            (1-args[index])**2)
        return r_sum
