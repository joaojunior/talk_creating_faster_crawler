asyncio:
	bash -c 'time python 1_crawler_with_async.py'

asyncio_uvloop:
	bash -c 'time python 2_crawler_with_async_uvloop.py'

benchmark:
	pytest crawler_benchmark.py  --benchmark-histogram --benchmark-min-rounds=5
