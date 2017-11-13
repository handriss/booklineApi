import urllib.parse as urlparse
from urllib.parse import urlencode
import urllib3


class MinimumPriceService:

    base_url = "https://bookline.hu/search/search.action"
    params = {
        'inner': 'true',
        'tab': 'bookline.hu/oldbook'
    }

    def __init__(self):
        self.http = urllib3.PoolManager()

    def build_url(self, author, title):
        current_params = self.params
        current_params['searchfield'] = author +  ": " + title

        url_parts = list(urlparse.urlparse(self.base_url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(current_params)

        url_parts[4] = urlencode(query)

        return urlparse.urlunparse(url_parts)

    def send_request(self, target_url):
        response = self.http.request('GET', target_url)
        print(response.data)



