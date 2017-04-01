#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 9 Part 1 Football Stats assignment"""

import urllib2
from bs4 import BeautifulSoup
import json

url = 'http://www.cbssports.com/nfl/stats/xsort/nfl/year-2016-season-regular-category-touchdowns'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')


def nfl_football_stats():
    """Some footballs stats from CBS for touchdowns."""
    touchdowns_list = []
    fhandler = soup.find_all(class_= {'row1', 'row2'})

    for touchdowns in fhandler[:20]:
        try:

        #x=players name; y=position of the players; z=z
            x = touchdowns.contents[0].get_text()
            
            y = touchdowns.contents[1].get_text()
            
            td = touchdowns.contents[6].get_text()
            
            z = touchdowns.contents[2].get_text()
            
            json_string = {
            "Players Name": x,
            "Position": y,
            "Touchdowns" : td,
            'Team' : z
            }
            print(json.dumps(json_string))

        except:
            print 'Error, Please try again later'
            continue

    return touchdowns_list

if __name__ == "__main__":
    nfl_football_stats()
