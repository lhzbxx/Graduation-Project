#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 09:01:04
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 09:01:38

import parser3


def main():
    p = parser3.Parser(1)
    a = p.parse()
    print a

if __name__ == '__main__':
    main()
