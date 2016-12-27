#!/usr/bin/env python
"""
Mutate a number of bit's in a string.
"""
import abc
import random

import six

from ag_frame.algorithms.representations.mutations import base


@six.add_metaclass(abc.ABCMeta)
class BitMutation(base.BaseMutation):
    """Base Bit Mutate.

    Change a number of bits.
    """

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    _name = "Bit Mutation"

    # pragma pylint: disable=unused-argument
    def __init__(self, bits_to_mutate=1):
        """Initializa the arguments.

        :param bits_to_shift: The number of bits to mutate.
        """
        self._bits_to_mutate = bits_to_mutate

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    def mutate(self, arg):
        """We will get a bite string and mutate a number of bits."""

        # normalize the number of bit's to mutate
        bits_to_mutate = self._bits_to_mutate % len(arg)

        # mask to keep track of the
        mask = [False for _ in range(len(arg))]
        arg = list(arg)
        for _ in range(bits_to_mutate):
            # get a random index to mutate
            index = None
            while not index or not mask[index]:
                index = random.randint(0, len(arg)-1)
                mask[index] = True

            if arg[index] == '0':
                arg[index] = '1'
            elif arg[index] == '1':
                arg[index] = '0'

        return "".join(arg)
