from multiprocessing import Pool

import requests

from constants import URL_FASTER, URL_SLOWLY


def crawler(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('error')
    return response.status_code


if __name__ == '__main__':
    p = Pool(21)
    urls = [URL_SLOWLY]

    for i in range(20):
        urls.append(URL_FASTER)

    p.map(crawler, urls)
