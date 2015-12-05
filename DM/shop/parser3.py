#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 09:02:06

from bs4 import BeautifulSoup
import requests
import time

class Parser():
    def __init__(self, i):
        self.url = 'http://www.dianping.com/shop/' + str(i)
    def parse(self):
        try:
            r = requests.get(str(self.url), timeout=1)
        except Exception, e:
            raise e
        soup = BeautifulSoup(r.text, "lxml")
        if soup.select(".main"):
            return repr(soup.select(".main")[0])
        else:
            return False

def main():
    p = Parser(1)
    a = p.parse()
    print a

if __name__ == '__main__':
    main()
