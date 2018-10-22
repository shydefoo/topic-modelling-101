from bs4 import BeautifulSoup
import requests
import pprint
from scrapers.base_scraper import BaseScraper

class CNAScraper(BaseScraper):
	@classmethod
	def get_text(cls, url):
	    res = requests.get(url, allow_redirects=False)
	    soup = BeautifulSoup(res.text, 'html.parser')
	    print("Prasing article..")
	    print(res.status_code)
	    return ''.join([_.get_text() for _ in soup.find_all('div', class_='c-rte--article')])

from sys import argv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, help='url to scrape')

if __name__ == '__main__':
	args = parser.parse_args(argv[1:])
	url = args.url	
	print(CNAScraper.get_text(url))
