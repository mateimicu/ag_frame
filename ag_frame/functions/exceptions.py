#!/usr/bin/env python
"""
Exception module for all exceptions.
"""
from ag_frame import exceptions


class ToFewArguments(exceptions.FunctionException):
    """Exception for when we try to call a function with to few argumensts."""
    MSG = "Function {} needs {} arguments but it got {}"

    def __init__(self, function_name=None, nr_args=None, given_nr_args=None):
        try:
            formated_msg = self.MSG.format(function_name,
                                           nr_args,
                                           given_nr_args)
        except TypeError:
            formated_msg = ("To few arguments fiven "
                            "to a AG Framework Function.")

        super(ToFewArguments, self).__init__(formated_msg)
