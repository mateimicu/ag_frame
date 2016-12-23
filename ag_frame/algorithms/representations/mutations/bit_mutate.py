#!/usr/bin/env python
"""
Mutate a number of bit's in a string.
"""
import abc
import random

import six

from ag_frame.algorithms.representations.mutations import base
from ag_frame.algorithms import utils


@six.add_metaclass(abc.ABCMeta)
class BitMutation(base.Base):
    """Base Bit Mutate.

    Change a number of bits.
    """

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    NAME = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, bits_to_mutate=1):
        """Initializa the arguments.

        :param bits_to_shift: The number of bits to mutate.
        """
        self._bits_to_mutate = bits_to_mutate

    def mutate(self, arg):
        """We will get a bite string and mutate a number of bits."""

        # normalize the number of bit's to mutate
        bits_to_mutate = self._bits_to_mutate % len(arg)

        # mask to keep track of the
        mask = [False for _ in range(len(arg))]
        for _ in range(bits_to_mutate):
            # get a random index to mutate
            index = None
            while not index or not mask[index]:
                index = random.randint(0, len(arg)-1)
            utils.mutate(arg, index)
