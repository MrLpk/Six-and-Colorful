#coding=utf-8
'''
Created on 2013-10-18

@author: liaopengkai
'''

import datetime
import time
import threading

class SynTask(threading.Thread):
    '''
    SynTask
    '''
    isRuning = False
    def waitToTomorrow(self, d = 0, h = 0, m = 0, s = 0):
        """定时器"""
        tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=d), hour=h, minute=m, second=s)
        delta = tomorrow - datetime.datetime.now()
        print '将休眠 ', delta
        time.sleep(delta.seconds)
        
    def run(self):
        d = 0
        h = 18
        m = 3
        s = 30
        self.isRuning = True
        while True:
            if self.isRuning:
                print 'do task'
            else:
                print 'not task'
            self.waitToTomorrow(d, h, m, s)
            s+=4
            print s
            if s >= 60:
                s=0
                m+=1
if __name__ == '__main__':
    pass
    s = SynTask()
#     s.start()
    print s.isRuning