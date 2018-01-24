#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from parse import MyHParser
from spider import NoteSpider

spider = NoteSpider()
html = spider.get_html()
hp = MyHParser()
hp.feed(html)
hp.save()
hp.close()
