from urllib.parse import urljoin


BASE_URL = 'http://127.0.0.1:4001/'

URL_TEXT = urljoin(BASE_URL, 'text')

NUMBER_REQUESTS = 10**6
BATCH_SIZE = 1000
