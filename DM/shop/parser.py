#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 07:33:52

from bs4 import BeautifulSoup
import requests
import time

class Parser():
    def __init__(self, i):
        self.url = 'http://www.dianping.com/shop/' + str(i)
    def parse(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "lxml")
        if soup.select(".main"):
            return repr(soup.select(".main")[0])
        else:
            return False
