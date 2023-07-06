#!/usr/bin/env python3
"""
11. More involved type annotations
"""

from typing import Mapping, Any, TypeVar, Union


T = TypeVAr('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ value from a dict using a given key"""
    if key in dct:
        return dct[key]
    else:
        return default
