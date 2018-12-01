import os


def test_crawler_with_asyncio(benchmark):
    benchmark(os.system, 'python 1_crawler_with_async.py')


def test_crawler_with_asyncio_uvloop(benchmark):
    benchmark(os.system, 'python 2_crawler_with_async_uvloop.py')
