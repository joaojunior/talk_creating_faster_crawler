import requests
import gevent.monkey
from gevent import Greenlet

from constants import BATCH_SIZE, NUMBER_REQUESTS, URL_FASTER

gevent.monkey.patch_socket()


def crawler(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('error')
    return response.status_code


if __name__ == '__main__':
    size = int(NUMBER_REQUESTS/BATCH_SIZE)
    for quantity in range(size):
        gthreads = []

        for i in range(BATCH_SIZE):
            gthreads.append(Greenlet(crawler, URL_FASTER))

        for gthread in gthreads:
            gthread.start()

        gevent.joinall(gthreads)
