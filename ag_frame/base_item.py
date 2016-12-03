#!/usr/bin/env python
"""
Base item for every in this library.
"""


# pragma pylint: disable=too-few-public-methods
class BaseItem(object):
    """Base class for every item."""
    _args = None

    @classmethod
    def set_args(cls, args):
        """Set the arguments."""
        cls._args = args
