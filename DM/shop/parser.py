#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 06:52:23

from bs4 import BeautifulSoup
import requests
import time


class Parser():
    url = ''
    def __init__(self, i):
        self.url = 'http://www.dianping.com/shop/' + str(i)
    def parse(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        if soup.select(".main"):

            print repr(soup.select(".main")[0])
        else:
            print 'bad'
print time.time()
r = requests.get('http://www.dianping.com/shop/504508')
soup = BeautifulSoup(r.text)
a = repr(soup.select(".main")[0])
f = open('123.txt', 'w')
f.write(a)
print time.time()
f = open('123.txt', 'r')
a = f.read()
soup = BeautifulSoup(a)
# print soup.select('.nug-shop-ab-special_a')[0]

r = requests.get('http://www.dianping.com/shop/1')
soup = BeautifulSoup(r.text)
if soup.select(".main"):
    print repr(soup.select(".main")[0])
else:
    print 'bad'
