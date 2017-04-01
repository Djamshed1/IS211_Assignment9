#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 9 Part 2 Apple Stock assignment"""

import urllib2
from bs4 import BeautifulSoup
import json

url = 'http://finance.yahoo.com/quote/AAPL/history?ltr=1'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'lxml')

def yahoo_apple_stock():
    data = []
    fhandler = soup.find_all('tr')

    for rows in fhandler:
        try:
            if len(rows.find_all(('td', {'class': 'yfnc_tabledata1'}))) == 7:
                close_price_date = rows.contents[0].get_text()
                close_price = rows.contents[6].get_text()
                data.append((close_price_date, close_price))
                json_string = {
                "Date for all closed prices": close_price_date,
                "The close price": close_price,
                }
                print(json.dumps(json_string))
        except:
            print 'Error, please try again later'
            continue
    return yahoo_apple_stock

if __name__ == "__main__":
    yahoo_apple_stock()
