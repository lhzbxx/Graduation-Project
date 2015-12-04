#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 03:24:49
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 07:05:28

from pymongo import MongoClient
import sqlite3

class Recorder():
    def __init__(self):
        print "Connect to database:",
        try:
            self.conn = sqlite3.connect('db/main.db')
        except Exception, e:
            print "[fail]"
            raise e
            return
        print "[success]"
    def record(self, id, content):
        self.conn.execute("INSERT INTO shop (id, content) \
            VALUES (" + id + ", " + content + ")");
        try:
            self.conn.commit()
        except Exception, e:
            raise e
            return False
        return True

# client = MongoClient()
# db = client.primer
# print db
