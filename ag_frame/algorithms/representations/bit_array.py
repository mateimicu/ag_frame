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
    _name = "bit_array"

    # pragma pylint: disable=unused-argument
    def __init__(self, nr_args, precision):
        """Initializa the arguments.

        :param nr_args: The number of arguments.
        """
        super(BitArray, self).__init__(nr_args)
        self._precision = precision

    def add_domains_restriction(self, domain_restriction):
        """Add the domain restrictions."""
        self._domain_restricion = domain_restriction
        self._size_var = self._get_size_var()
        self._nr_of_bits = self._get_nr_of_bits()

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

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

    def get_random(self):
        """Get a random genom."""
        base_genom = "1" * sum(self._size_var)
        return utils.randomise_a_string(base_genom)

    def encode(self, args):
        """Encode the arguments."""
        to_return = ""
        for index, arg in enumerate(args):
            nr_bits = utils.get_nr_bits(self._domain_restricion[index],
                                        self._precision)
            domain_lenght = (self._domain_restricion[index][1]
                             - self._domain_restricion[index][0])

            num = (arg * (2 ** nr_bits - 1) -
                   self._domain_restricion[index][0])
            bit = int((num / domain_lenght))
            str_bit = "{0:b}".format(bit)
            if len(str_bit) < nr_bits:
                str_bit = str_bit.zfill(nr_bits - len(str_bit))

            to_return = to_return + str_bit

        return to_return

    def decode(self, args):
        """Decode the arguments."""
        return utils.string_to_args(args, self._size_var,
                                    self._domain_restricion,
                                    self._precision)
