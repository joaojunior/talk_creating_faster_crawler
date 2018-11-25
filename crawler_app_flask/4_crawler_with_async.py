import asyncio
import aiohttp


from constants import URL_FASTER, URL_SLOWLY


async def crawler(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status != 200:
            print('error')
        return response.status


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    futures = [asyncio.ensure_future(
        crawler(URL_SLOWLY)
    )]

    for i in range(20):
        futures.append(asyncio.ensure_future(crawler(URL_FASTER)))
    loop.run_until_complete(asyncio.gather(*futures))
