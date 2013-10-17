#coding=utf-8

import json

def createSQL():

	fi = open('json/2012.json', 'r').read()
	js = json.loads(fi)
	print js['year']
	data = js['data']
	# for item in data:
	for i in range(5):
		item = data[i]
		# print item
		d = item['d']
		normal = '%s,%s,%s,%s,%s,%s' %(d[0],d[1],d[2],d[3],d[4],d[5])
		s = u"insert into sac(year,time,no,normal,special) values(%s, '%s', '%s', '%s', '%s')" %(js['year'], item['t'], item['n'], normal, item['s'])
		print s

if __name__ == '__main__':

	createSQL()