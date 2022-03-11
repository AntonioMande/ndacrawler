import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('cache.sqlite3')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

url = "https://www.nda.or.ug/drug-register"

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
