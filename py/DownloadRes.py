'''
Created on 2013-10-14

@author: liaopengkai
'''
import os
from MTool import MTool

if __name__ == '__main__':
    
    path = 'htmlRes/'
    fromYear = 2005
    toYear   = 2013
    
    m = MTool()
    
    if not os.path.isdir(path):
        os.mkdir(path)
    
    time = toYear - fromYear + 1
    for i in range(time):
        url = 'http://www.111kj.com/kjjg/%d.htm' %fromYear

        m.download(url, path)
        fromYear = fromYear+1
        
    print 'download files succeed'
    
    
    
    