#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 06:20:36

from pymongo import MongoClient
import sqlite3

class Recorder():
    def __init__(this, id, content):
        conn = sqlite3.connect('test.db')


# client = MongoClient()
# db = client.primer
# print db
