## Introduction

This repo contains the code for the presentation **Creating a faster crawler** that I presented at
PyMalta on December 5, 2018.
In the presentation I showed how to work with blocking IO and non-blocking IO in Python.
You can access the slides of this presentation in my website: http://joaojunior.org/presentations/creating-a-faster-crawler/

## Requirements
To run the examples here is required the python >= 3.6.5 and install the libraries in the `requirements.txt`.
To install all the libraries, run the command: `pip install -r requirements.txt`

## How to run the examples
We have 3 examples here: The first example make 21 requests, the second example make 10k requests with batch of 100 requests
and the last example make 1 million requests with batch of 1k requests.

To run the first example, go to the folder `app_flask` and run the server with the command: `make example_1`.
After this, you can go to the folder `crawler_app_flask` and run the command `make benchmark` to generate all the benchmark.

To run the second example, go to the folder `app_flask` and run the server with the command: `make example_2`.
After this, you can go to the folder `crawler_app_flask_many_requests` and run the command `make benchmark` to generate all the benchmark.

To run the last example, go to the folder `app_flask` and run the server with the command: `make example_2`.
After this, you can go to the folder `crawler_app_flask_many_requests` and run the command `make benchmark` to generate all the benchmark.


## Folder Structure
```
.
├── app_flask
│   ├── app.py
│   └── Makefile
├── changelog.md
├── crawler_app_flask
│   ├── 1_crawler_sequential.py
│   ├── 2_crawler_with_threads.py
│   ├── 3_crawler_with_green_threads.py
│   ├── 4_crawler_with_async.py
│   ├── 5_crawler_with_multiprocessing.py
│   ├── constants.py
│   ├── crawler_benchmark.py
│   └── Makefile
├── crawler_app_flask_1_million_requests
│   ├── 1_crawler_with_async.py
│   ├── 2_crawler_with_async_uvloop.py
│   ├── constants.py
│   ├── crawler_benchmark.py
│   └── Makefile
├── crawler_app_flask_many_requests
│   ├── 1_crawler_with_threads.py
│   ├── 2_crawler_with_green_threads.py
│   ├── 3_crawler_with_async.py
│   ├── constants.py
│   ├── crawler_benchmark.py
│   └── Makefile
├── LICENSE
├── README.md
└── requirements.txt

4 directories, 25 files
```
