#coding=UTF-8
'''
Created on 2013年8月4日

@author: DY
'''

import re
from MTool import MTool
import json

def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close() 
    print 'save done'

def one():
    m = MTool()
    
    obj = [
           {'year':2012,
           'data':[
                   {'date':'','no':1,'num':[1,2,3,4,5,6],'special':7},
                   {'no':2,'num':[11,12,13,14,15,16],'special':18}
                   ]
           }
           ]
    abc = json.dumps(obj)
    #     print abc
    m.save('t.json', abc)
    
    f = open('t.json', 'r')
    content = f.read()
    
    cc = json.loads(content)
    print cc[0]

def save2012():
    f = open('htmlRes/2012.htm', 'r')
    content = f.read()
        
    key1 = r'<font face="Terminal">([^ ]*)</font></td>'
    result1 = re.findall(key1, content)
        
    key2 = '<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">([^\t]*gif">*)</td>'
    result2 = re.findall(key2, content)
        
    key3 = '<td width="77" align="center" valign="middle" bgcolor="#FFFFFF"><IMG src="49m/([0-9]*).gif"></td>'
    result3 = re.findall(key3, content)
        
        #    print 'reuslt1 = \n', result1
        #     print 'reuslt2 = \n', result2
        #     print 'reuslt3 = \n', result3
        
        #     print '\nitem ='
        #     for item in result2:
        #         print item
        #         print '----------------------------'
        
        
        
    print 'reuslt1 num = ', len(result1)
    print 'reuslt2 num = ', len(result2)
    print 'reuslt3 num = ', len(result3)
    
    arr = []
    for i in range(152):
        
        k = '<IMG src="49m/([0-9]*).gif"'
        r = re.findall(k, result2[i])
#        print result2[i]
#        print r
#        print '*'*10
        
        t = result1[i*2]
        n = result1[i*2+1]
        d = r
        s = result3[i]
        
        obj = {'t':t,
               'n':n,
               'd':d,
               's':s
            }
        
        arr.append(obj)
    result = {'year':2012, 'data':arr}
    j = json.dumps(result)
    m = MTool()
    m.save('2012.json', j, False, 'json/')

#    fi = open('json/2012.json', 'r').read()
#    js = json.loads(fi)
#    print js
#    print js['year']

def save2011():
    f = open('htmlRes/2011.htm', 'r')
    content = f.read()
    
    key1 = r'<font face="Terminal">([^ ]*)</font></td>'
    result1 = re.findall(key1, content)
    
    key2 = '<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">([^\t]*gif">*)</td>'
    result2 = re.findall(key2, content)
    
    key3 = '<td width="77" align="center" valign="middle" bgcolor="#FFFFFF"><IMG src="49m/([0-9]*).gif"></td>'
    result3 = re.findall(key3, content)
    
    #    print 'reuslt1 = \n', result1
    #     print 'reuslt2 = \n', result2
    #     print 'reuslt3 = \n', result3
    
    #     print '\nitem ='
    #     for item in result2:
    #         print item
    #         print '----------------------------'
    
    
    
    print 'reuslt1 num = ', len(result1)
    print 'reuslt2 num = ', len(result2)
    print 'reuslt3 num = ', len(result3)
    
    arr = []
    for i in range(154):
        
        k = '<IMG src="49m/([0-9]*).gif"'
        r = re.findall(k, result2[i])
        #        print result2[i]
        #        print r
        #        print '*'*10
        
        t = result1[i*2]
        n = result1[i*2+1]
        d = r
        s = result3[i]
        
        obj = {'t':t,
            'n':n,
            'd':d,
            's':s
            }
        
        arr.append(obj)
    result = {'year':2011, 'data':arr}
    j = json.dumps(result)
    m = MTool()
    m.save('2011.json', j, False, 'json/')

#    fi = open('json/2012.json', 'r').read()
#    js = json.loads(fi)
#    print js
#    print js['year']

def save20xx(y, num):
    f = open('htmlRes/%d.htm' %y, 'r')
    content = f.read()
    
    key1 = r'<font face="Terminal">([^ ]*)</font></td>'
    result1 = re.findall(key1, content)
    
    key2 = '<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">([^\t]*gif">*)</td>'
    result2 = re.findall(key2, content)
    
    key3 = '<td width="77" align="center" valign="middle" bgcolor="#FFFFFF"><IMG src="49m/([0-9]*).gif"></td>'
    result3 = re.findall(key3, content)
    
    #    print 'reuslt1 = \n', result1
    #     print 'reuslt2 = \n', result2
    #     print 'reuslt3 = \n', result3
    
    #     print '\nitem ='
    #     for item in result2:
    #         print item
    #         print '----------------------------'
    
    
    
    print 'reuslt1 num = ', len(result1)
    print 'reuslt2 num = ', len(result2)
    print 'reuslt3 num = ', len(result3)
    
    arr = []
    for i in range(num):
        
        k = '<IMG src="49m/([0-9]*).gif"'
        r = re.findall(k, result2[i])
        #        print result2[i]
        #        print r
        #        print '*'*10
        
        t = result1[i*2]
        n = result1[i*2+1]
        d = r
        s = result3[i]
        
        obj = {'t':t,
            'n':n,
            'd':d,
            's':s
        }
        
        arr.append(obj)
    result = {'year':y, 'data':arr}
    j = json.dumps(result)
    m = MTool()
    m.save('%d.json'%y, j, False, 'json/')

#    fi = open('json/2012.json', 'r').read()
#    js = json.loads(fi)
#    print js
#    print js['year']

def save20xx_1(y, num):
    f = open('htmlRes/%d.htm' %y, 'r')
    content = f.read()
    
    key1 = r'<font face="Terminal">([^ ]*)</font></td>'
    result1 = re.findall(key1, content)
    
    key2 = '<td width="187" align="center" valign="bottom" bgcolor="#FFFFFF">([^\t]*gif">*)</td>'
    result2 = re.findall(key2, content)
    
    key3 = 'align="center" valign="middle" bgcolor="#FFFFFF"><IMG src="49m/([0-9]*).gif"></td>'
    result3 = re.findall(key3, content)
    
    #    print 'reuslt1 = \n', result1
    #     print 'reuslt2 = \n', result2
    #     print 'reuslt3 = \n', result3
    
    #     print '\nitem ='
    #     for item in result2:
    #         print item
    #         print '----------------------------'
    
    
    
    print 'reuslt1 num = ', len(result1)
    print 'reuslt2 num = ', len(result2)
    print 'reuslt3 num = ', len(result3)
    
    arr = []
    for i in range(num):
        
        k = '<IMG src="49m/([0-9]*).gif"'
        r = re.findall(k, result2[i])
        #        print result2[i]
        #        print r
        #        print '*'*10
        
        t = result1[i*2]
        n = result1[i*2+1]
        d = r
        s = result3[i]
        
        obj = {'t':t,
            'n':n,
            'd':d,
            's':s
        }
        
        arr.append(obj)
    result = {'year':y, 'data':arr}
    j = json.dumps(result)
    m = MTool()
    m.save('%d.json'%y, j, False, 'json/')

#    fi = open('json/2012.json', 'r').read()
#    js = json.loads(fi)
#    print js
#    print js['year']



if __name__ == '__main__':


    
#    key2 = r'<IMG src[0-9A-Za-z ="/.<>\n]*.gif">'   //half good
       
#    key2 = r'<(IMG src.*)</td>'

#    key2 = '#FFFFFF">\n([0-9A-Za-z ="/.<>  \n]*)\b</td>'


#    save2012()
#    save2011()
#    save20xx(2010, 152)
#    save20xx(2009, 154)
    save20xx_1(2008, 149)


    
    
    
    