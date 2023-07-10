#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

asyncio def wait_n(n: int, max_delay: int) -> List[float]:
    delays_list = [wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(delay_time)]
