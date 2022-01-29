# !/usr/bin/env python
# -*-coding:utf-8 -*-

from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from plyer import notification

def neiwang():
    time.sleep(2)
    browser = webdriver.Chrome()
    browser.get("https://office.postoa.com.cn/jt/login.jsp")
    time.sleep(1)
    browser.find_element(By.ID,"details-button").click()
    time.sleep(1)
    browser.find_element(By.ID,"proceed-link").click()
    browser.maximize_window()
    time.sleep(5)
    browser.find_element(By.ID,"memberName").send_keys("身份证")
    time.sleep(1)
    browser.find_element(By.ID,"parampw").send_keys("密码")
    time.sleep(1)
    browser.find_element(By.CLASS_NAME,"code_btn").click()
    time.sleep(60)
    return '执行中'

def wangluo_test():
    print("开始测试网络")
    flag = 0
    while flag == 0:
        try:
            se = requests.get(url="https://www.baidu.com/")
        except:
            time.sleep(2)
            print('尝试中')
            continue
        else:
            print('开始执行脚本')
            nei=neiwang()
            print(nei)
            flag == 1
            time.sleep(2)
            break
        finally:
            print('执行完毕')

t = time.localtime(time.time())
hr = t.tm_hour
if hr >= 8 | hr <9:
    print('时间检验合格')
    wangluo_test()
else:
    print('不在时间范围')
    notification.notify(
        title="内网登录提醒",
        message="不在时间范围内",
        timeout=5
    )
