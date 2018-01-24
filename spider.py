#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
class NoteSpider:
    def get_html(self):
        cookie = cookielib.CookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookie_handler)
        url = "https://app.yinxiang.com/HeaderLogin.action"
        loginheaders = {
            "Host": "app.yinxiang.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Content-Length": "173",
        }

        data = {
            "username": "example@mail.com",
            "password": "123456",
            "login": "",
            "_sourcePage": "OvWWzkA91tDiMUD9T65RG_YvRLZ-1eYO3fqfqRu0fynRL_1nukNa4gH1t86pc1SP",
            "__fp": "0S936uHrSyQ3yWPvuidLz-TPR6I9Jhx8"
        }
        data = urllib.urlencode(data)
        print data
        request = urllib2.Request(url, data=data, headers=loginheaders)
        response_login = opener.open(request)

        url_note = "https://app.yinxiang.com/shard/s16/nl/19039186/8c2671d4-439c-4979-a3e7-aed85a39cb42?content="
        noteheaders = {
            "Host": "app.yinxiang.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Referer": "https://app.yinxiang.com/shard/s16/nl/19039186/8c2671d4-439c-4979-a3e7-aed85a39cb42",
            # "Cookie":'''notelinkAuth="S=s16:U=12283d2:E=161c1809898:C=1612701d09b:P=5fd:A=en-web:V=2:H=cae0212bbef348bf09dd30174ddfc923\""; referral=mktg_hp; gr_user_id=45466b34-a148-4f8e-ab34-029e7903b753; _ga=GA1.2.719104702.1516761253; _gid=GA1.2.974031142.1516761253; cookieTestValue=1516770926406; JSESSIONID=8C7F985BE788ED50417F9539EDF2EE1A; utag_main=v_id:01612604137800657c8549c5a8b40004e003e00d00bd0$_sn:3$_ss:0$_st:1516779703146$dc_visit:3$ses_id:1516775589362%3Bexp-session$_pn:15%3Bexp-session$dc_event:33%3Bexp-session$dc_region:us-east-1%3Bexp-session; userdata_lastLoginTime=1516777885857; userdata_accountType=PREMIUM; userdata_acctCreatedTime=1508132240000; lastAuthentication=1516777885867/eb9b80aee907a0672661b33ec40ab2cf; web50017PreUserGuid=eec517dc-7da2-4e8f-8402-259aa0c8e581; rem_user=wang.hongji%40foxmail.com; enAppInstalled=false; gr_session_id_a8c147a9b6c5c9bb=1d3aed6b-c0a1-426c-9bfe-6539f9387e78; req_sec="U=12283d2:P=/:E=1612710a72f:S=e2856d7c2e0d7fa5c5b6ab3b0003cd0c"; auth="S=s16:U=12283d2:E=161c1809898:C=1612701d09b:P=5fd:A=en-web:V=2:H=cae0212bbef348bf09dd30174ddfc923"; userdata_loggedIn=true; clipper-sso="S=s16:U=12283d2:E=1687eb2fca7:C=1612701d0a8:P=1d5:A=en-chrome-clipper-xauth-new:V=2:H=5911d89d2a65c05fa7c9bdbb177709a1"''',
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        request_note = urllib2.Request(url_note, headers=noteheaders)
        response_note = opener.open(request_note)
        return response_note.read()

