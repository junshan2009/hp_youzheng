# !/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re
import time
import pandas as pd

from ugirlsfile.zijichangshi import get_pic

mm = """https://www.ugirl.com"""
res_dict = ["""https://www.ugirl.com/meinvtupian/6729.html"""]
flag = 1
infores=[]

def get_url(url):
    res = requests.get(url=url)
    res.encoding = 'utf-8'
    soup = bs(res.text, "html.parser")
    f1 = soup.findAll("div", attrs={"class": re.compile("bar-item")})
    res2 = ''
    for f22 in f1:
        s2 = f22.get_text()
        s3 = re.search("上一期", s2)
        if s3:
            s4 = str(f22)
            s5 = s4.find("""href="/""")
            s6 = s4.find(""".html""")
            ss2 = s4[s5 + 6:s6 + 5]
            res2 = mm + ss2
            # print(res2)
    return res2


while flag:
    print(res_dict[-1])
    sm1 = get_url(res_dict[-1])
    sm2 = get_pic.picget(sm1)
    infores.append(sm2)
    res_dict.append(sm1)
    flag = len(sm1)
    time.sleep(2)

df=pd.DataFrame({
    'a': res_dict,
    'info':infores
} )

df.to_csv('111.csv')