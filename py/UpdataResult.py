#coding=utf-8

import urllib2
import re
def request1():
	url1 = 'http://kj.4394.com/kj/scores.xml'
	r1 = urllib2.urlopen(url1).read().decode('gb2312')

	key = '<score>([\w\W]*)</score>'
	f = re.findall(key, r1)

	key1 = '\n([0-9]*),'
	v1 = re.findall(key1, f[0])

	key2 = ',(\S*) '
	v2 = re.findall(key2, f[0])

	key3 = ':([0-90]*)'
	v3 = re.findall(key3, f[0])
	print 'r1 = \n',r1
	print f
	print 'v1 = ',v1
	print 'v2 = ',v2
	print 'v3 = ',v3
	
def  request2():
	url2 = 'http://kj.4887.com/kj/'
	r2 = urllib2.urlopen(url2).read().decode('gbk')

	print 'r2 = \n',r2.decode('gbk')
if __name__ == '__main__':
	request1()
	request2()