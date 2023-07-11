#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension four times in parallel using asyncio.gather.
    measures the total runtime and return it
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
