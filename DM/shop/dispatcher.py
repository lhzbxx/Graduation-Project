#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuHao
# @Date:   2015-12-05 06:05:08
# @Last Modified by:   LuHao
# @Last Modified time: 2015-12-05 07:57:01


import parser2
import recorder
import config

import Queue
import threading
import time

exit_flag = 0
work_queue = []
queue_lock = threading.Lock()
threads = []
blank_page = 0
good_page = 0
work_process = config.THREAD_NUM

process_msg = 'blank_page:' + str(blank_page) + '\ngood_page:' + str(good_page) + '\n' + str(work_queue)

for i in range(config.THREAD_NUM):
    i += 1
    work_queue.append(i)

class Dispatcher(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.recorder = recorder.Recorder()
    def run(self):
        while not exit_flag:
            queue_lock.acquire()
            id = work_queue.pop()
            work_process += 1
            work_queue.append(work_process)
            queueLock.release()
            if work_queue:
                p = parser2.Parser(id)
                con = p.parse()
                if(con):
                    self.recorder.record(id, con)
                    update_msg('good')
                else:
                    update_msg('blank')

def update_msg(msg):
    print '\b' * len(process_msg),
    if msg == 'good':
        good_page += 1
    if msg == 'blank':
        blank_page += 1
    process_msg = 'blank_page:' + str(blank_page) + '\ngood_page:' + str(good_page) + '\n' + str(work_queue)

for i in range(config.THREAD_NUM):
    thread = Dispatcher()
    thread.start()
    threads.append(thread)

while work_process <= config.MAX_PAGE_NUM:
    pass

exit_flag = 1

print "End at: " + str(time.time())

for t in threads:
    t.join()
