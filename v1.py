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

#    save('six.txt', result)
    result = result.decode('gbk')
#
    key = r'<font face="Terminal">([^ ]*)</font></td>'
    title = re.findall(key, result)
#    print 'title = \n', title
    
#    key2 = r'<IMG src[0-9A-Za-z ="/.<>\n]*.gif">'   //half good
    
#    w = '''<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">
#<IMG src="49m/48.gif"> <IMG src="49m/46.gif"> <IMG src="49m/33.gif"> <IMG src="49m/32.gif"> <IMG src="49m/25.gif"> <IMG src="49m/17.gif"></td>'''
    
#    key2 = r'<(IMG src.*)</td>'

#    key2 = '#FFFFFF">\n([0-9A-Za-z ="/.<>  \n]*)\b</td>'
    key2 = '<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">\n([\s\S]*gif">*)</td>'
    
    f = open('six.txt', 'r')
    a = f.read()
    
    w = '''     <tr>
        <td width="119" align="center" valign="middle" bgcolor="#FFFFFF">
        <font face="Terminal">2012/10/30</font></td>
        <td width="62" align="center" valign="middle" bgcolor="#FFFFFF">
        <font face="Terminal">125</font></td>
        <td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">
        <IMG src="49m/40.gif"> <IMG src="49m/1.gif"> <IMG src="49m/28.gif"> <IMG src="49m/34.gif"> <IMG src="49m/20.gif"> <IMG src="49m/30.gif"></td>
        <td width="77" align="center" valign="middle" bgcolor="#FFFFFF"><IMG src="49m/19.gif"></td>
        <td width="60" align="center" valign="middle" bgcolor="#FFFFFF">
        <font face="Fixedsys">172</font></td>
        <td width="181" align="center" valign="middle" bgcolor="#FFFF99">
        <font style="font-size: 9pt">¹·.µ¥Êý.Ð¡Êý.ºì²¨.¼ÒÐó</font></td>
        </tr>'''

    title2 = re.findall(key2, a)
#    print a
    
    
    print 'title2 = \n', title2
    
#    print '\nitem ='
#    for item in title2:
#        print item
#        print '----------------------------'
    
    print 'title num = ', len(title)
    print 'title2 num = ', len(title2)

            
            
            
            
    
    
    
    
    