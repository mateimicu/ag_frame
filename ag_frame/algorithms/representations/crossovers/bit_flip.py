#!/usr/bin/env python

"""
Crossover flip a bit.
"""
import abc
import random

import six

from ag_frame.algorithms.representations.crossovers import base


@six.add_metaclass(abc.ABCMeta)
class BitCut(base.BaseCrossover):
    """Base Crossover.

    This crossover chooses a random N >= 0 <= min(len(arg1), len(args2)).
    """

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    NAME = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, *args, **kwargs):
        """Initializa the arguments."""
        super(BitCut, self).__init__(*args, **kwargs)
        self._precision = kwargs.pop("precision", .5)

    def crossover(self, arg1, arg2):
        """Return a list with the new crossoverd items.

        Returns a list with the new genoms.
        :param arg1: First genom
        :param arg2: Second genom
        """
        # max length
        max_len = min(len(arg1), len(arg2)) - 1

        if not max_len:
            return arg1, arg2

        child1 = ""
        child2 = ""

        for index in range(max_len):
            if random.random() < self._precision:
                # swap
                child1 += arg2[index]
                child2 += arg1[index]
            else:
                child1 += arg1[index]
                child2 += arg2[index]

        # if the genoms have diferite lenghts
        child1 += arg1[max_len:]
        child2 += arg2[max_len:]

        return child1, child2
