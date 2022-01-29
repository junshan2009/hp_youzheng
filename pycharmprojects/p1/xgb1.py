# !/usr/bin/env python
# -*-coding:utf-8 -*-

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv(r'D:\work\12\2\xgbdemodata.csv')
# print(df.head())

#下面对字符变量进行数字化处理--------------------------------LabelEncoder()
le = LabelEncoder()
lb_list = ["AS", "AV", "BS", "BV"]
le.fit(lb_list)
print(le.classes_)  # 输出为：['amsterdam' 'paris' 'tokyo']
city_list_le = le.transform(lb_list)  # 进行Encode
#开始进行编码
lb=df['lb']
print(lb)
lb_encode=le.transform(lb)
print(lb_encode)
df['lb_en']=lb_encode
print(df.head())
#
# print(city_list_le)  # 输出为：[1 1 2 0]
# city_list_new = le.inverse_transform(city_list_le)  # 进行decode
# print(city_list_new)  # 输出为：['paris' 'paris' 'tokyo' 'amsterdam']


# 下面进行one-hot的字符串编码
from sklearn.preprocessing import OneHotEncoder
