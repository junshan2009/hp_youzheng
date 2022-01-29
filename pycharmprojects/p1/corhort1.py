# !/usr/bin/env python
# -*-coding:utf-8 -*-
import  pandas as pd
import pyodbc
cnxn =pyodbc.connect(DSN='tableau')
cursor =cnxn.cursor()
sql='''select * from bkg.corhort'''
df=pd.read_sql(sql,cnxn)
print(df)
for i in range(100000000):
    print(i)


