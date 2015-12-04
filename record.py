#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 03:42:53

from pymongo import MongoClient
import sqlite3


conn = sqlite3.connect('test.db')
print "Opened database successfully";
client = MongoClient()
db = client.primer
print db

print 'ok'
