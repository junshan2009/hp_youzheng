# !/usr/bin/env python
# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Kline
import webbrowser

df=pd.read_csv(r'D:\work\11\24\klines.csv',encoding='gbk')
print(df.head())

df2=df[['月初','月末','最高','最低']]

np1=df2.values.tolist()
print(np1)
print(type(np1))

np2=df['省份'].values.tolist()
print(np2)

c = (
    Kline()
    .add_xaxis(np2)
    .add_yaxis(
        "各省份营业K线图",
        np1,
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="max", value_dim="close")]
        ),
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        title_opts=opts.TitleOpts(title="my_kline"),
    )
    .render("my_kline.html")
)

webbrowser.open("my_kline.html")