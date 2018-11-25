import requests
import gevent.monkey
from gevent import Greenlet

from constants import URL_FASTER, URL_SLOWLY

gevent.monkey.patch_socket()


def crawler(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('error')
    return response.status_code


if __name__ == '__main__':
    gthreads = [Greenlet(crawler, URL_SLOWLY)]

    for i in range(20):
        gthreads.append(Greenlet(crawler, URL_FASTER))

    for gthread in gthreads:
        gthread.start()

    gevent.joinall(gthreads)
