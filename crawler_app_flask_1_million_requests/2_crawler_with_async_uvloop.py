import asyncio

import aiohttp
import uvloop

from constants import BATCH_SIZE, NUMBER_REQUESTS, URL_TEXT

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def crawler(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status != 200:
            print('error')
        return response.status


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    size = int(NUMBER_REQUESTS/BATCH_SIZE)

    for quantity in range(size):
        futures = []

        for i in range(BATCH_SIZE):
            futures.append(asyncio.ensure_future(crawler(URL_TEXT)))
        loop.run_until_complete(asyncio.gather(*futures))
