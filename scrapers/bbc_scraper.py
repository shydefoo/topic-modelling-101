from bs4 import BeautifulSoup
import requests
import pprint
from scrapers.base_scraper import BaseScraper

class BBCScraper(BaseScraper):
	@classmethod
	def get_text(cls, url):
	    res = requests.get(url, allow_redirects=False)
	    soup = BeautifulSoup(res.text, 'html.parser')
	    print("Prasing article..")
	    print(res.status_code)
	    story_body = soup.find(class_='story-body')
	    all_p_list = story_body.find_all('p')
	    return ''.join([_.get_text() for _ in all_p_list if not _.has_attr('aria-hidden')])
