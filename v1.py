#coding=UTF-8
'''
Created on 2013年8月4日

@author: DY
'''

import urllib2
import re

def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close() 
    print 'save done'
    
if __name__ == '__main__':

    url = 'http://www.111kj.com/kjjg/2012.htm'

    result = urllib2.urlopen(url).read()

#     save('six.txt', result.decode('gbk'))
    result = result.decode('gbk')
    
    key = r'<font face="Terminal">([^ ]*)</font></td>'
    title = re.findall(key, result)
    print 'title = \n', title
    
#     key2 = r'<IMG src.+if">'
    w = '''<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">
<IMG src="49m/48.gif"> <IMG src="49m/46.gif"> <IMG src="49m/33.gif"> <IMG src="49m/32.gif"> <IMG src="49m/25.gif"> <IMG src="49m/17.gif"></td>'''
#    key2 = '.*</td>'

    key2 = r'\S*</td>'
    title2 = re.findall(key2, w)
    print 'title2 = \n', title2
    
    print 'title num = ', len(title)
    print 'title2 num = ', len(title2)        
            
            
            
            
            
    
    
    
    
    