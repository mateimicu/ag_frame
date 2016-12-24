#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Selections.
"""
import abc

import six

from ag_frame import base_item
from ag_frame import exceptions
from ag_frame.functions import base


@six.add_metaclass(abc.ABCMeta)
class BaseSelection(base_item.BaseItem):
    """Base class for every function.

    Every function should implement this methods.
    """

    _name = "Basic Selection"

    def __init__(self, selected_number, function, representaion, *kwargs):
        """Initialize an Selection algorithm.

        :param selected_number: The number of genomes we want to select.
        :param function: The function we use for selecting them.
        :param representaion: What representation is used.
        """
        self._selected_number = selected_number
        self._funcion = function
        self._representation = representaion

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
        """Split the list with populations in two.

        The first part will be the selected part, and the second one the rest.
        """
        pass
