#coding=UTF-8
'''
Created on 2013年8月4日

@author: DY
'''

import re

def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close() 
    print 'save done'
    
if __name__ == '__main__':


    
#    key2 = r'<IMG src[0-9A-Za-z ="/.<>\n]*.gif">'   //half good
       
#    key2 = r'<(IMG src.*)</td>'

#    key2 = '#FFFFFF">\n([0-9A-Za-z ="/.<>  \n]*)\b</td>'

    f = open('htmlRes/2012.htm', 'r')
    content = f.read()

    key1 = r'<font face="Terminal">([^ ]*)</font></td>'
    result1 = re.findall(key1, content)


    key2 = '<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">([^\t]*gif">*)</td>'
    result2 = re.findall(key2, content)
    
    key3 = '<td width="77" align="center" valign="middle" bgcolor="#FFFFFF"><IMG src="49m/([0-9]*).gif"></td>'
    result3 = re.findall(key3, content)
    
#     print result1
#     print 'title2 = \n', result2
#     print result3
    
#     print '\nitem ='
#     for item in result2:
#         print item
#         print '----------------------------'
        

    
    print 'reuslt1 num = ', len(result1)
    print 'reuslt2 num = ', len(result2)
    print 'reuslt3 num = ', len(result3)

            
            
            
            
    
    
    
    
    