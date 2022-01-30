# !/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re
import os

def picget(url):
    res = requests.get(url=url)
    res.encoding = 'utf-8'
    soup = bs(res.text, "html.parser")
    f1 = soup.findAll("img", attrs={"src": re.compile("album")})
    f2 = soup.findAll("span", attrs={"class": "value"})
    info = ''
    for f22 in f2:
        info = info + str(f22.get_text())
    info = re.sub(",", "", info).replace("/", "").replace(" ", "")
    n1 = 0
    for f11 in f1:
        # print(f11)
        # print(f11['src'])
        s1 = f11['src']
        n1 += 1
        finame = "sss/{}s{}.jpg".format(info, n1)
        req = requests.get(s1)
        if len(req.content) > 100000:
            with open(finame, "wb") as f:
                f.write(req.content)
    return info