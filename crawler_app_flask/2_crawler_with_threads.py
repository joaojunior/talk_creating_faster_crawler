from threading import Thread

import requests

from constants import URL_FASTER, URL_SLOWLY


def crawler(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('error')
    return response.status_code


if __name__ == '__main__':
    threads = [Thread(target=crawler, args=(URL_SLOWLY,))]

    for i in range(20):
        t = Thread(target=crawler, args=(URL_FASTER,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
