#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""weathereek 9 Part 3 Monthly Temperature assignment"""

import urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('https://weatherweatherweather.weatherunderground.com/history/airport/KNYC/2015/1/1/MonthlyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.weathermo=')
soup = BeautifulSoup(html)

def main():
    monthly_weathereather = soup.findAll('table', {"class": 'dateTable'})
    for weather in monthly_weathereather:
        if weather.find('a', {"class": "dateText"}) is None:
            pass
        else:
            date = weather.find('a', {"class": "dateText"}).get_text()
        if weather.find('td', {"class": "value-header"}, text=['Actual:', 'Forecast:']) is None:
            pass
        else:
            typeoftemp = weather.find('td', {"class": "value-header"}, text=['Actual:', 'Forecast:']).get_text()
            if weather.find('span', {"class": "high"}) is None:
                pass
            else:
                high = weather.find('span', {"class": "high"}).get_text()[:2]
            if weather.find('span', {"class": "loweather"}) is None:
                pass
            else:
                low = weather.find('span', {"class": "loweather"}).get_text()[:2]
            print "date of Month: {}, Temp Type: {}, High: {}, Loweather: {}".format(date, typeoftemp, high, low)

if __name__ == '__main__':
    main()
