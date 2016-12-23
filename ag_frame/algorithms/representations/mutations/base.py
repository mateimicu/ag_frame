#!/usr/bin/env python

"""
"""
import abc

import six

from ag_frame import base_item


@six.add_metaclass(abc.ABCMeta)
class BaseMutation(base_item.BaseItem):
    """Base Mutation."""

    # If this is a combinatoric representation
    COMBINATORIC = False

    # The name of the array
    NAME = "Base"

    # pragma pylint: disable=unused-argument
    def __init__(self, *args, **kwargs):
        """Initializa the arguments."""

    @abc.abstractmethod
    def mutate(self, args)
