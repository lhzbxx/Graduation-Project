#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 06:25:14
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 07:16:08

import dispatcher

def main():
    d = Dispatcher()
    d.dispatch()

if __name__ == '__main__':
    print "Begin at: " + str(time.time())
    main()
