sequential:
	bash -c 'time python 1_crawler_sequential.py'

threads:
	bash -c 'time python 2_crawler_with_threads.py'

gthreads:
	bash -c 'time python 3_crawler_with_green_threads.py'

asyncio:
	bash -c 'time python 4_crawler_with_async.py'

benchmark:
	pytest crawler_benchmark.py  --benchmark-histogram --benchmark-min-rounds=100
