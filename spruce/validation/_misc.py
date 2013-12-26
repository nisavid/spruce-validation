"""Validation miscellany."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

from collections import namedtuple as _namedtuple


class UnexpectedValue(_namedtuple('UnexpectedValue', ('actual', 'expected'))):
    """An unexpected value.

    :param object actual:
        The actual value.

    :param object expected:
        The expected value.

    """
    pass
