#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 03:26:29

from pymongo import MongoClient

client = MongoClient()
db = client.primer
print db

print 'ok'
