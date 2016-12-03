#!/usr/bin/env python

"""
Representations for a set of inputs.
"""
import abc

import six

from ag_frame import base_item

# NOTE(mmicu): This is not that good of an idea,
# we need to use mixin or something like that
# to make sure the mutation and crossover are allowed on
# this representation


@six.add_metaclass(abc.ABCMeta)
class BaseRepresentation(base_item.BaseItem):
    """Base Representation."""

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    NAME = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, nr_args, *args, **kwargs):
        """Initializa the arguments.

        :param nr_args: The number of arguments.
        """
        self._nr_args = nr_args

    @classmethod
    def add_parser(cls, base_parser):
        """Add the informations about the representations to the cli."""
        pass

    @abc.abstractmethod
    def encode(self, args):
        """Encode the arguments."""

    @abc.abstractmethod
    def decode(self, args):
        """Decode the arguments."""
