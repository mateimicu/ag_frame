#!/usr/bin/env python

"""
Crossover base.
"""
import abc
import random

import six

from ag_frame.algorithms.representations.crossovers import base


@six.add_metaclass(abc.ABCMeta)
class BitCut(base.BaseCrossover):
    """Base Crossover.

    This crossover chooses a random N >= 0 <= min(len(arg1), len(args2)).
    Cut the genomes at the N bit then swap the first part and connect them.
    """

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    _name = "Bit Cut"

    # pragma pylint: disable=unused-argument
    def __init__(self, *args, **kwargs):
        """Initializa the arguments."""
        super(BitCut, self).__init__(*args, **kwargs)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

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

        if not len(arg1) or not len(arg2):
            return arg1, arg2

        cut = random.randint(1, max_len)
        child1 = arg1[:cut] + arg2[cut:]
        child2 = arg2[:cut] + arg1[cut:]


        return child1, child2
