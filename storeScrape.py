import requests
from bs4 import BeautifulSoup
import html5lib


class Tracker:
    def __init__(self,amazon='https://www.amazon.com/Xbox-X/dp/B08H75RTZ8', walmart='https://www.walmart.com/ip/Xbox-Series-X/141335186', target='https://www.target.com/p/xbox-series-x-console/-/A-80790841'):
        self.amazon = amazon
        self.walmart = walmart
        self.target = target
        self.prices = self.getPrices(self.amazon, self.walmart, self.target)
    
    def getPrices(self, amazon, walmart, target):
        #WWALMART Section
        wally = requests.get(walmart).text
        wally_soup = BeautifulSoup(wally, 'html5lib')
        if str(wally_soup.find('div', attrs={'class': 'error-message-margin error-page-message'})):
            wal_price = None
        else:
            wal_price = 'something is here'
        #More walmart info here for successful run

        #AMAZON section
        amz = requests.get(amazon).text
        amz_soup = BeautifulSoup(amz, 'html5lib')
        if not amz_soup.find('input', attrs={'id':'add-to-cart-button'}):
            amz_price = None
        else:
            pass
            #More amazon info here for successful run

        #TARGET section
        targ = requests.get(target).text
        targ_soup = BeautifulSoup(targ, 'html5lib')
        if str(targ_soup.find('div', attrs={'data-test':'notAvailableForShippingMessage'})):
            targ_price = None
        else:
            pass
            # More target for successful run here        
        return {'Walmart': wal_price,
                'Amazon': amz_price,
                'Target': targ_price}

print(Tracker().prices)


