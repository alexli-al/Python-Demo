# -*- coding:utf-8 -*-
# https://cuiqingcai.com/990.html
import urllib
import urllib2
import re
import json


class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = {'User-Agent': self.user_agent}
		self.stories = []
		self.enable = False

	def getPage(self, pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/'+ str(pageIndex)
			# create request
			request = urllib2.Request(url, headers = self.headers)
			# get page via urlopen
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			# print pageCode
			return pageCode
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print 'Fail to connect the XiuBai',  e.reason
				return None

	def getAllStroy(self, pageCode):
		if not pageCode:
			print "Fail to load the page"
			return None
		pattern = re.compile('<div.*?author.*?<h2>(.*?)</h2>.*?<div.*?content.*?<span>(.*?)</span>.*?stats-vote.*?number">(.*?)</i>',re.S|re.M)
		items = re.findall(pattern, pageCode)
		pageSrories = []
		for item in items:
			# print item[0]			
			pageSrories.append([item[0].replace("\n",''), item[1].replace("\n",''),  item[2]+"\n\n" ])
			# pageSrories.append("Nickname:"+ item[0].replace("\n",'')).
		# # return pageSrories
		print self.decode(pageSrories)

	# handle the mass code
	def decode(self, code):
		if not code:
			return None
		return json.dumps(code, encoding="UTF-8", ensure_ascii=False)


if __name__ == "__main__":
	spider = QSBK()
	spider.getAllStroy(spider.getPage(2))
	# spider.getPage(2)


