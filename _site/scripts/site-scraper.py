'''
    dependencies:
        requests
            http://www.python-requests.org/
            pip install requests

        beautifulsoup4
            http://www.crummy.com/software/BeautifulSoup/
            pip install beautifulsoup4
'''

import sys
import requests
from bs4 import BeautifulSoup

base_url = 'http://iccf-holland.org/'

def get_soup(url):
    r = requests.get(base_url + url)
    return BeautifulSoup(r.text)

soup = get_soup('indexn.html')

def get_urls(soup):
    urls = {}
    for link in soup.find_all('a'):
        url = link.get('href')
        title = link.text
        if not url in urls and link.string is not None:
            urls[url] = {
                'url': url,
                'title': title
            }
    return urls

urls = get_urls(soup)

for url in urls:

    if url.startswith('http'):
        continue

    soup = get_soup(url)

    urls[url]['children'] = get_urls(soup)

print urls
