#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Selections.
"""
import abc

import six

from ag_frame import base_item
from ag_frame import exceptions
from ag_frame.functions import base as base_function
from ag_frame.algorithms.representations import base as base_repr


@six.add_metaclass(abc.ABCMeta)
class BaseSelection(base_item.BaseItem):
    """Base class for every function.

    Every function should implement this methods.
    """

    _name = "Basic Selection"

    def __init__(self, representaion, *kwargs):
        """Initialize an Selection algorithm.

        :param representaion: What representation is used.
        """
        if not isinstance(representaion, base_repr.BaseRepresentation):
            raise TypeError("This is not a representation!")
        self._representation = representaion

    def add_function(self, function):
        """Add the function in case

        :param function: The function we use for selecting them.
        """
        if not isinstance(function, base_function.Function):
            raise TypeError("This is not a function!")
        self._function = function


    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.SelectionNotImplemented("Not Implemented.")

    @classmethod
    def name(cls):
        """Return the name of the function in a standard format."""
        return cls._name.replace(" ", "_").lower()

    @classmethod
    def pretty_name(cls):
        """Return the name of the function in a pretty format."""
        return cls._name

    @abc.abstractmethod
    def select(self, population):
        """Select a cromozom and return the population."""
        pass
