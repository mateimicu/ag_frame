#!/usr/bin/env python

"""
Representations for a set of inputs.
"""

from ag_frame.algorithms.representations import base
from ag_frame.algorithms import utils


class BitArray(base.BaseRepresentation):
    """Base Representation."""

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    NAME = "bit_array"

    # pragma pylint: disable=unused-argument
    def __init__(self, nr_args, precision, domain_restriction):
        """Initializa the arguments.

        :param nr_args: The number of arguments.
        """
        super(BitArray, self).__init__(nr_args)
        self._precision = precision
        self._domain_restricion = domain_restriction
        self._size_var = self._get_size_var()
        self._nr_of_bits = self._get_nr_of_bits()

    def _get_size_var(self):
        """Get the size of every variable."""
        size_var = []
        for index in range(self._nr_args):
            restriction = self._domain_restricion[index]
            size_var.append(utils.get_nr_bits(restriction, self._precision))
        return size_var

    def _get_nr_of_bits(self):
        """Get the number of bits needed for an item."""
        return sum(self._size_var)

    @classmethod
    def add_parser(cls, base_parser):
        """Add the informations about the representations to the cli."""
        pass

    def encode(self, args):
        """Encode the arguments."""
        to_return = ""
        # TODO(mmicu): Implement this

        return to_return

    def decode(self, args):
        """Decode the arguments."""
        return utils.string_to_args(args, self._size_var,
                                    self._domain_restricion,
                                    self._precision)
