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

urls = []

for link in soup.find_all('a'):
    # turn any relative urls into absolute urls
    url = urljoin(base, link.get('href'))
    host = urlparse(url).netloc

    if host != base_host:
        urls.append(url)

def unique(items):
    """Return a list of the unique items and how many times each occurs"""
    prev = None
    count = None
    uniques = []

    for item in sorted(items):
        if prev == None:
            count = 1

        elif prev == item:
            count = count + 1

        else:
            uniques.append((prev, count))
            count = 1
        
        prev = item

    if prev != None:
        uniques.append((prev, count))

    return uniques

for (url, count) in unique(urls):
    print(f'{url}: {count}')
