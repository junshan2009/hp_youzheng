# !/usr/bin/env python
# -*-coding:utf-8 -*-

import folium
import webbrowser
m=folium.Map(location=[40.009867,116.485994],zoom_start=10) # 绘制地图，确定聚焦点

folium.Marker([40.2,116.7],popup='<b>浮标上面的那个文字</b>').add_to(m)  # 定一个点，放到地图m上
folium.Marker([40.22,116.72],popup='浮标上面的那个文字',icon=folium.Icon(color='red')).add_to(m)
# 把浮标变成红色
folium.Marker([40.24,116.74],popup='<b>浮标上面的那个文字</b>',icon=folium.Icon(color='green',icon='info-sign')).add_to(m)
# 浮标改图样

#标记一个空心的圈
folium.Circle(
    location=[40.2,117.7],
    radius=10000,
    color='crimson',
    popup='popup',
    fill=False
).add_to(m)

#标记一个实心圆
folium.CircleMarker(
    location=[39.2,117.7],
    radius=100,
    popup='popup',
    color='#DC143C',#圈的颜色
    fill=True,
    fill_color='#6495ED' #填充颜色
).add_to(m)
m.save('f1.html')
webbrowser.open('f1.html')
