import requests

from constants import URL_FASTER, URL_SLOWLY


def crawler(url):
    response = requests.get(url)
    return response.status_code


if __name__ == '__main__':
    crawler(URL_SLOWLY)

    for i in range(6):
        crawler(URL_FASTER)
