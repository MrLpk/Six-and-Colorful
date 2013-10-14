#-*- coding: utf-8 -*-
'''
Created on 2013-8-27

@author: liaopengkai
'''
import urllib2
import os

class MTool:
    
    def isNum(self, tempStr):
        """判断字符串是否为数字，整型和浮点型皆适用"""
        try:
            float(tempStr)
            return True
        except Exception:
            return False
        
    def save(self, filename, contents, reNew = True, path = ''):
        '''保存文件，参数:文件名、内容、是否覆盖更新、路径'''
        if path != '':
            filename = path + filename
        if os.path.exists(filename):
            if not reNew:
                print 'You already have ' + filename
                return
        fh = open(filename, 'w') 
        fh.write(contents.decode('gbk')) 
        fh.close() 
#         print filename
        print 'Save '+filename+' success...'
        
    def download(self, url, path = '', reNew = True):
        '''下载并保存'''
        result = urllib2.urlopen(url).read()
        temp = url.split('/')
        name = temp[len(temp)-1]
        self.save(name, result, reNew, path)
        
if __name__ == '__main__':
    pass
#     url = 'http://www.111kj.com/kjjg/2012.htm'
#     m = MTool()
#     m.download(url, 't/')

    