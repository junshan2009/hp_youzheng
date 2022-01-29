# !/usr/bin/env python
# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import os
import folium
from folium import plugins
import webbrowser
#import geopandas as gp
from folium.plugins import HeatMap

#数据导入：
full = pd.read_csv(r"D:\work\11\24\city_geo.csv")
posi = full.dropna()
print(posi.head())

lat = np.array(posi["纬度"][0:len(posi)])
lon = np.array(posi["经度"][0:len(posi)])
pop = np.array(posi["pop"][0:len(posi)],dtype=float)

#data1 = [[lat[i],lon[i],pop[i]] for i in range(len(posi))]
data1 = [[lat[i],lon[i],0.02] for i in range(len(posi))]

#创建以高德地图为底图的密度图：
map_osm = folium.Map(
    location=[35,110],
    zoom_start=5,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
    attr="""&copy; <a href="http://ditu.amap.com/">高德地图</a>"""
    )
#创建以腾讯地图为底图的密度图：
# map_osm = folium.Map(
#     location=[35,110],
#     zoom_start=5,
#     tiles='http://rt{s}.map.gtimg.com/realtimerender?z={z}&x={x}&y={y}&type=vector&style=0',
#     attr="""&copy; <a href="http://map.qq.com/">腾讯地图</a>"""
#     )
#生成交互式地图：
HeatMap(data1).add_to(map_osm)
file_path = "People.html"
map_osm.save(file_path)
webbrowser.open(file_path)
