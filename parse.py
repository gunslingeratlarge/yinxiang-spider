#!/usr/bin/env python
#! -*- coding:utf-8 -*-
import HTMLParser
from createdocx import MyDoc
import datetime

class MyHParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.a_title = False
        self.start = False
        self.mydoc = MyDoc()
        time = datetime.datetime.today()
        date = str(time.strftime('20%y%m%d'))
        self.mydoc.add_title("周报告"+'-'+date)
        self.mydoc.add_heading2("一、概述")
        self.mydoc.add_para("这个星期是一个比较充实的星期，我初步了解了xxx的使用，熟悉了xxx，并对xxx有了更为深入的认识。同时还进行了xxx的学习，并结合xxx")
        self.mydoc.add_heading2("二、具体内容")

    def handle_starttag(self, tag, attrs):
         for attr in attrs:
             if attr[1] == "ennote":
                 self.start = True
    def handle_data(self, data):
        if(data != ""  and  self.start == True):
            self.mydoc.add_para(data)
    def save(self):
        self.mydoc.save("周报告.docx")

# hp = MyHParser()
# with open("a.html","r") as f:
#     html = f.read()
# hp.feed(html)
# hp.save()
# hp.close()