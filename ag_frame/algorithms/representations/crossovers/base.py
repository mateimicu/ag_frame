#!/usr/bin/env python

"""
Crossover base.
"""
import abc

import six

from ag_frame import base_item
from ag_frame import exceptions


@six.add_metaclass(abc.ABCMeta)
class BaseCrossover(base_item.BaseItem):
    """Base Crossover."""

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    _name = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, *args, **kwargs):
        """Initializa the arguments."""

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.CrossoverNotImplemented("Not Implemented.")

    @classmethod
    def name(cls):
        """Return the name of the function in a standard format."""
        return cls._name.replace(" ", "_").lower()

    @classmethod
    def pretty_name(cls):
        """Return the name of the function in a pretty format."""
        return cls._name

    def crossover(self, arg1, arg2):
        """Return a list with the new crossoverd items."""
