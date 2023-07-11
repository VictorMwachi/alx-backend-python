#!/usr/bin/env python3

import asyncio
import random
from typing import Generator 


async async_generator() -> Generator[float,None,None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randrange(0, 10)
