# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()


class BDTB:

    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz='+ str(seeLZ)
        self.tool = Tool()
        self.floor = 1
        self.file = open("text.txt", "w+")

    def getPage(self, pageIndex):
        try:
            url = self.baseUrl + self.seeLZ + '&pn' + str(pageIndex)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
            # print response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "Fail to connect tieba", e.reason
                return None

    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S | re.M)
        return self.getSpecificInfo(pattern, page)

    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?red.*?>(.*?)</span>',re.S | re.M)
        return self.getSpecificInfo(pattern, page)

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>.*?</cc>', re.S | re.M)
        items = re.findall(pattern, page)
        # for item in items:
        #     print floor, u"楼----------------------------------------------"
        #     print self.tool.replace(item)
        #     print '\n'
        #     floor += 1
        self.writeData(items)

    def writeData(self, content):
        for item in content:
            floorLine = "\n" + str(self.floor) + u" floor ------------------------------------\n"
            self.file.write(floorLine)
            print self.tool.replace(item)
            self.file.write(self.tool.replace(item))
            self.file.write("\n")
            self.floor += 1


    # tool method
    def getSpecificInfo(self, pattern, page):
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

if __name__ == "__main__":
    baseUrl = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseUrl,1)
    page = bdtb.getPage(1)
    # bdtb.getPage(1)
    # print 'Title:', bdtb.getTitle(page)
    # print 'Replied Count:', bdtb.getPageNum(page)
    bdtb.getContent(page)





