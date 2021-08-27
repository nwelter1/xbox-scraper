# spin-button-children
from bs4 import BeautifulSoup
import requests
import html5lib
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
def getPrice(walmart):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(walmart)
    html = driver.page_source
    wally_soup = BeautifulSoup(html, 'html5lib')
    if wally_soup.find('div', attrs={'class': 'error-message-margin error-page-message'}):
        wal_price = None
    else:
        wal_price = wally_soup.find('span', attrs={'itemprop': 'price'})
    return wal_price['content']

print(getPrice('https://www.walmart.com/ip/Xbox-Series-S/606518560'))