from threading import Thread

import requests

from constants import BATCH_SIZE, NUMBER_REQUESTS, URL_FASTER


def crawler(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('error')
    return response.status_code


if __name__ == '__main__':
    size = int(NUMBER_REQUESTS/BATCH_SIZE)
    for quantity in range(size):
        threads = []

        for i in range(BATCH_SIZE):
            t = Thread(target=crawler, args=(URL_FASTER,))
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()
