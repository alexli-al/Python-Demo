**  Python理论上支持无限位运算
C实现无限位运算？
传统的数据结构无法解决，链表 小数点后面当作字符串来看，只要内存够大，就能进行无限位运算

** Ipython 安装 pip install ipython


** sublime 字体：
"font_size": 12,
"font_face": "Comic Sans MS"
crtrl+shif+p package controll 安装插件

** 开启Vim模式：
Preferences -> Setting - User 即可打开配置文件进行编辑，将 ignored_packages 项的[]里面内容清空："ignored_packages": []
ESC进入command模式，a进入编辑（插入）模式

ctrl+b 直接运行在sublime中运行python
ctrl+d 退出python 


** pip install requests
request. + tab 查看requests中的全部类

** 爬虫百度
import requests
res=requests.get("http://www.baidu.com")
saveFile=open("baidu.html", "w")
saveFile.write(res.content)
saveFile.close()


** 学习语法用Ipython，coding用sublime

raw_input()：接收用户输入
列表list ==>数组有[]
元组truple ==>只读的列表 ()
字典 dictironary ==> {key: value ，key1: value1} json

Python资料
 https://pan.baidu.com/s/1geBnhRl 密码: 7qdc
 二次解压密码：www.snowfox.wang

 python setup.py build
 python setup.py sdist

File 结构体
Mode: r+
 读写指针位置， seek()设置读写指针位置
 文件描述符
 缓冲区地址指针

 fflush()刷新缓冲区

 pip install -I --no-cache-dir -v Pillow
 PIL: http://effbot.org/imagingbook/


**   'str' object has no attribute 'isdecimal', only for unicode, replace with isdigit()

** Log
# -*- coding: utf-8 -*-
import logging,re 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# logging.disable(logging.CRITICAL)


pip install mysqlclient
http://blog.csdn.net/qq_26808915/article/details/50256717


full-stack:
https://github.com/phodal/growth-in-action
https://github.com/phodal
https://www.cnblogs.com/xzjs/p/5527731.html

blog: root/root1234

urls：http://blog.csdn.net/feelang/article/details/25245935

Python Demo
https://zhuanlan.zhihu.com/p/22164270
https://zhuanlan.zhihu.com/p/22164270
https://www.zhihu.com/question/29372574/answer/88624507

爬虫
http://blog.csdn.net/wxg694175346/article/category/1418998/1
https://cuiqingcai.com/927.html





