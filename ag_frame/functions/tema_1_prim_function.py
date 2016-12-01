#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Mathematical functions.
"""
import math

from ag_frame.functions import base


class Tema1Func(base.Function):
    """Function used just as an example."""

    _name = "Tema1Function"

    def __init__(self):
        """Initialize this function.

        :param dimensions: The number of dimension ( The default one is 8 )
        """
        local_mins = (
            tuple([0 for _ in range(1)]),
        )
        super(Tema1Func, self).__init__(
            nr_args=1, default_domain=(0, 31),
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
        cls.parser = base_parser.add_parser(cls.name(),
                                            help="Run this function.")

    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        # f=x3-60x2+900x+100
        var = args[0]
        return var ** 3 - 60 * var ** 2 + 900 * var + 100
