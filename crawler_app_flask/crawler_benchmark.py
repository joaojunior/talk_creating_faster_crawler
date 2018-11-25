import os


def test_crawler_with_threads(benchmark):
    benchmark(os.system, 'python 2_crawler_with_threads.py')


def test_crawler_with_green_threads(benchmark):
    benchmark(os.system, 'python 3_crawler_with_green_threads.py')


def test_crawler_with_asyncio(benchmark):
    benchmark(os.system, 'python 4_crawler_with_async.py')
