example_1:
	gunicorn -w 4 -b 127.0.0.1:4000 app:app

example_2:
	# Don't use -w equal numbers of simultaneous connections. It is only for test
	gunicorn -w 100 -b 127.0.0.1:4001 app:app
