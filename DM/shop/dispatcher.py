#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 06:05:08
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 09:05:55


import parser3
import recorder
import config

import Queue
import threading
import time

class Dispatcher(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.recorder = recorder.Recorder()
    def run(self):
        while not exit_flag:
            global work_process
            queue_lock.acquire()
            shop_id = work_process
            work_process += 1
            queue_lock.release()
            p = parser3.Parser(shop_id)
            a = p.parse()
            if(con):
                self.recorder.record(shop_id, con)
                update_msg('good')
            else:
                update_msg('blank')

def update_msg(msg):
    print '\b' * len(process_msg),
    if msg == 'good':
        good_page += 1
    if msg == 'blank':
        blank_page += 1
    process_msg = 'blank_page:' + str(blank_page) + '\ngood_page:' + str(good_page)
    print process_msg

exit_flag = 0
queue_lock = threading.Lock()
threads = []
blank_page = 0
good_page = 0
work_process = 1

process_msg = 'blank_page:' + str(blank_page) + '\ngood_page:' + str(good_page)

for i in range(config.THREAD_NUM):
    thread = Dispatcher()
    thread.start()
    threads.append(thread)

while work_process <= config.MAX_PAGE_NUM:
    time.sleep(0.001)

exit_flag = 1

print "End at: " + str(time.time())

for t in threads:
    t.join()
