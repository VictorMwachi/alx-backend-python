#!/usr/bin/env python3
"""
10. Duck typing - first element of a sequence
"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a sequence if exists else None is returned"""
    if lst:
        return lst[0]
    else:
        return None
