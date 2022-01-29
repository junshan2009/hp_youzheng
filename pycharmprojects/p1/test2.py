# !/usr/bin/env python
# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import re

df=pd.read_excel(r'D:\work\12\user_udc.xls',sheet_name='Sheet1')
print(df.head())
lall=[]
lall2=[]
for row in df.iterrows():
    l1=[]
    l2=[]
    r2=list(row)
    # print(r2[1][1])
    s1=r2[1][1]
    r1=re.findall("延期到|时效过长|迟不送|快递时效|取件|揽件|发货|配送慢|没有按时|物流太慢|约定时间|超时|还不发|不送货|未按照|不送达|未及时|未送达",s1)
    if len(r1)>0:
        l1.append('总体速度慢')
        l2.append('time_1')
    r2=re.findall("一直不送|发错地址|寄错地方|地址错误|按照配送地址|发错地址|不给派件|不配送|延误|派送|不投递|配送超时|不派件|不送件|未配送|到达营业点",s1)
    if len(r2)>0:
        l1.append('派送不及时')
        l2.append('time_4')
    r3 = re.findall("赔付|押金|不按商品金额赔付|保价|不赔|赔偿|理赔|不退款|不予退款", s1)
    if len(r3) > 0:
        l1.append('赔偿不到位')
        l2.append('service_4')
    r4 = re.findall("客服不处理", s1)
    if len(r4) > 0:
        l1.append('投诉无响应')
        l2.append('service_2')
    r4 = re.findall("碎了|有损|磕碰|破损|损坏|损毁", s1)
    if len(r4) > 0:
        l1.append('邮件破损')
        l2.append('quality_2')
    r5 = re.findall("私自签收|签收问题|默认签收", s1)
    if len(r5) > 0:
        l1.append('私自签收不通知')
        l2.append('quality_6')
    r6 = re.findall("丢重要件|未收到|漏发|丢件|丢失|漏了|没收到", s1)
    if len(r6) > 0:
        l1.append('邮件缺失')
        l2.append('quality_3')
    r7 = re.findall("迟不处理|仍旧寄出|服务不到位|久不处理|一直不处理|迟不回复", s1)
    if len(r7) > 0:
        l1.append('响应不到位')
        l2.append('service_3')
    r8 = re.findall("售后服务|客服", s1)
    if len(r8) > 0:
        l1.append('客服人员服务态度差')
        l2.append('attitude_5')
    r9 = re.findall("配送人员电话关机|快递员们服务态度|快递小哥有点歪|不予拒收|辱骂|快递员态度问题|私拆快递|快递员拒收|快递不接电话|快递员辱骂|派送员态度|快递员骂人|快递员素质|派件员", s1)
    if len(r9) > 0:
        l1.append('配送人员服务态度差')
        l2.append('attitude_4')
    r10 = re.findall("不揽收|上门|未显示揽收|退货快递员|拒收不退回|拒不揽收", s1)
    if len(r10) > 0:
        l1.append('上门揽收不及时')
        l2.append('time_2')
    r11 = re.findall("串货|实物不符|配送错误|虚假|自动退回|分拣错误|发错货|恶意掉包|发错货", s1)
    if len(r11) > 0:
        l1.append('物流信息异常')
        l2.append('quality_1')
    r12 = re.findall("物流信息|未更新|没有及时更新|更改地址|查不到|一直显示|一直停在|一直不更新|物流不动|物流持续不更新|一直不动|不更新|没有更新|不动了|物流没更新", s1)
    if len(r12) > 0:
        l1.append('物流信息更新不及时')
        l2.append('quality_5')
    r13 = re.findall("计重错误|收费|续费|多收", s1)
    if len(r13) > 0:
        l1.append('乱收费')
        l2.append('price_1')
    r14 = re.findall("不告知|快递员取消|未经同意|私自|放自提点|私自更改|未经本人允许|自己做主|丰巢|提前签收|擅自|自动修改|私自修改|显示已签收", s1)
    if len(r14) > 0:
        l1.append('擅自修改配送时间、方式')
        l2.append('quality_7')
    r15=re.findall('拒收后不发',s1)
    if len(r15)>0:
        l1.append('服务中断')
        l2.append('quality_4')
    r16=re.findall('站点',s1)
    if len(r16)>0:
        l1.append('中转时间长')
        l2.append('time_3')
    lall.append(l1)
    lall2.append(l2)

print(lall)
df['findall']=lall
df['namelist']=lall2
df.to_excel('myresult.xls',encoding='utf-8')
print(df)





