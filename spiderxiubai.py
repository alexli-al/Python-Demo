# -*- coding:utf-8 -*-
# https://cuiqingcai.com/1052.html
# http://blog.csdn.net/eastmount/article/details/51082253
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# add header otherwise it will throw BadStatusLine error
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	# file = open('save.txt','w')
	# file.write(content)
	# file.close()

	# .*?  (.*?)
	pattern = re.compile('<div.*?author.*?<h2>(.*?)</h2>.*?<div.*?content.*?<span>(.*?)</span>.*?stats-vote.*?number">(.*?)</i>',re.S|re.M)
	items = re.findall(pattern, content)
	for item in items:
		# print item
		# haveImg = re.search("img", item[3])
		# if not haveImg:
		print "Nickname:" + item[0].replace("\n",''), "\nContent: "+ item[1].replace("\n",''),  "\nVote: "+ item[2]+"\n\n"
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason