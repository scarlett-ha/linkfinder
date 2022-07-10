import requests
import argparse
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='find unique URLs on a given web page')
parser.add_argument('baseurl', help='the url of the web page')
args = parser.parse_args()

base = args.baseurl
base_host = urlparse(base).netloc

r = requests.get(base)

soup = BeautifulSoup(r.content, 'lxml')

urls = set()

for link in soup.find_all('a'):
    # turn any relative urls into absolute urls
    url = urljoin(base, link.get('href'))
    host = urlparse(url).netloc

    if host != base_host:
        urls.add(url)

for url in sorted(urls):
    print(url)
