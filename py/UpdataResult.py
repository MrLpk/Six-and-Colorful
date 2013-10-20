#coding=utf-8

import urllib2
import re
import json
from MTool import MTool

def save(obj):
	j = json.dumps(obj)
	m = MTool()
	m.save('kj.json', j, True)

def request1():
	url1 = 'http://kj.4394.com/kj/scores.xml'
	r1 = urllib2.urlopen(url1).read().decode('gb2312')

	key = '<score>([\w\W]*)</score>'
	f = re.findall(key, r1)

	key1 = '\n([0-9]*),'
	v1 = re.findall(key1, f[0])

	key2 = ',(\S*) '
	v2 = re.findall(key2, f[0])

	key3 = ':([0-9]*)'
	v3 = re.findall(key3, f[0])
	print 'r1 = \n',r1
	print f
	print 'v1 = ',v1
	print 'v2 = ',v2
	print 'v3 = ',v3
	
def  request2():
	url2 = 'http://kj.4887.com/kj/'
	r2 = urllib2.urlopen(url2).read().decode('gbk')

	print 'r2 = \n',r2

	key = 'none">([\s\S]*)</span></a></div>'
	f = re.findall(key, r2)[0]
	print 'v = ',f

	key1 = '([\d]{3})'
	v1 = re.findall(key1, f)[0]

	key2 = ':([\d-]*) '
	v2 = re.findall(key2, f)[0]

	key3 = ':(\d{1,2})'
	v3 = re.findall(key3, f)

	key4 = '>(\d{1,2})</font></b>'
	v4 = re.findall(key4, r2)
	print 'v1 = ',v1
	print 'v2 = ',v2
	print 'v3 = ',v3[1]
	print 'v4 = ',v4

	v2 = v2.split('-')
	for i in range(len(v2)):
		v2[i] = int(v2[i])
	print 'v2 - ',v2
	t = '2013/%s/%s' %(v4[0], v4[1])
	n = v1
	d = v2
	s = v3[1]
	obj = {'t':t,
            'n':n,
            'd':d,
            's':s
        }

	f = open('kj.json', 'r').read()
	js = json.loads(f)
	if v1 == js['n']:
		print 'true'
	else:
		print 'false'
if __name__ == '__main__':

	try:
		request1()
		request2()
	except Exception:
		print 'net error'
	