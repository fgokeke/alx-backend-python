#!/usr/bin/env python3

"""a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime by executing async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    end_time = time()
    total_runtime = end_time - start_time

    return total_runtime
