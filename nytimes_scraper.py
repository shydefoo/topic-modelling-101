from bs4 import BeautifulSoup
import requests
import pprint

def get_text(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    print("Prasing article..")
    return ''.join([_.get_text() for _ in soup.find_all('p', class_='css-1xl4flh e2kc3sl0')])
