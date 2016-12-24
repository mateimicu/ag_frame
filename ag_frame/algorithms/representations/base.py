#!/usr/bin/env python

"""
Representations for a set of inputs.
"""
import abc

import six

from ag_frame import base_item
from ag_frame import exceptions


@six.add_metaclass(abc.ABCMeta)
class BaseRepresentation(base_item.BaseItem):
    """Base Representation."""

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    _name = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, nr_args, *args, **kwargs):
        """Initializa the arguments.

        :param nr_args: The number of arguments.
        """
        self._nr_args = nr_args

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.RepresentationNotImplemented("Not Implemented.")

    @classmethod
    def name(cls):
        """Return the name of the function in a standard format."""
        return cls._name.replace(" ", "_").lower()

    @classmethod
    def pretty_name(cls):
        """Return the name of the function in a pretty format."""
        return cls._name

    @abc.abstractmethod
    def encode(self, args):
        """Encode the arguments."""

    @abc.abstractmethod
    def decode(self, args):
        """Decode the arguments."""
