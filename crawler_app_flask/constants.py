from urllib.parse import urljoin


BASE_URL = 'http://127.0.0.1:4000'

URL_SLOWLY = urljoin(BASE_URL, 'slowly')
URL_FASTER = urljoin(BASE_URL, 'faster')
