#!/usr/bin/env python3
"""
0. The basics of async
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """returns delay time await time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
