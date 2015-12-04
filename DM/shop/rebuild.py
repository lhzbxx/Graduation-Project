#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 06:19:23
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 06:24:03


import os
import create_db

def main():
    os.remove(os.path.join(os.path.join(os.path.dirname(__file__), 'db'), 'main.db'))
    create_db.init_db()

if __name__ == '__main__':
    main()
