# !/usr/bin/env python
# -*-coding:utf-8 -*-
from selenium import webdriver
import requests

import time
time.sleep(5)
browser = webdriver.Chrome()


browser.get("https://office.postoa.com.cn/jt/login.jsp")
time.sleep(1)
browser.find_element_by_id("details-button").click()
time.sleep(1)
browser.find_element_by_id("proceed-link").click()
time.sleep(2)
browser.find_element_by_id("memberName").send_keys("341204199006241216")
time.sleep(1)
browser.find_element_by_id("parampw").send_keys("@Junshan2009")
time.sleep(1)
browser.find_element_by_class_name("code_btn").click()

# browser.quit()
