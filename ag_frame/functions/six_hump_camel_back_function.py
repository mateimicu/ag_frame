#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
he 2-D Six-hump camel back function [DS78] is a global optimization
test function. Within the bounded region are six local minima,
two of them are global minima.
"""
from ag_frame.functions import base


class SixHumpCamelBackFunction(base.Function):
    """Six-hump camel back function."""
    _name = "Rosenbrock's valley"

    def __init__(self):
        local_mins = (
            (-0.0898, 0.7126),
            (0.0898, -0.7126)
        )
        super(SixHumpCamelBackFunction, self).__init__(
            nr_args=2, default_domain=(-3, 3),
            local_mins=local_mins)

    def prepare_domain_restrictions(self):
        """This method add the specific domain restriction.

        This method should be overwirten if we have specific domain
        restrictions for any argument. By default it does nothing.
        """
        self.add_specific_domain_restriction(1, (-3, 3))
        self.add_specific_domain_restriction(2, (-2, 2))

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    @classmethod
    def add_parser(cls, base_parser):
        """Add the default parser for this function.

        :param parser: The top-level parser
        """
        cls.parser = base_parser.add_parser(cls.name(),
                                            help="Run this function.")

    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        # fSixh(x1,x2) = (4-2.1·x1^2+x1^4/3)·x1^2+x1·x2+(-4+4·x2^2)·x2^2
        left_side = (4 - 2.1 * args[0]**2 + args[0] ** (4/3)) * args[0]**2
        middle_side = args[0] * args[1]
        right_side = (-4 + 4 * args[1]**2) * args[1] ** 2
        return left_side + middle_side + right_side
