from urllib.parse import urljoin


BASE_URL = 'http://127.0.0.1:4001'

URL_FASTER = urljoin(BASE_URL, 'faster')

NUMBER_REQUESTS = 10000
BATCH_SIZE = 100
