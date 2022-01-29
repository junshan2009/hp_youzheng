# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
   绘制gps轨迹图
   :param locations: list, 需要绘制轨迹的经纬度信息，格式为[[lat1, lon1], [lat2, lon2], ...]
   :param output_path: str, 轨迹图保存路径
   :param file_name: str, 轨迹图保存文件名
   :return: None
"""

import folium
import webbrowser

m=folium.Map(location=[40.009867,116.485994],zoom_start=10) # 绘制地图，确定聚焦点
locations_true=[[39.789692,116.501625],[39.807509,116.536172],[39.811839,116.531279]]
folium.PolyLine(  # polyline方法为将坐标用实线形式连接起来
    locations_true,  # 将坐标点连接起来
    weight=4,  # 线的大小为4
    color='red',  # 线的颜色为红色
    opacity=0.8,  # 线的透明度
    #dash_array='5'  虚线频率
).add_to(m)  # 将这条线添加到刚才的区域m内

m.save('f_line.html')
webbrowser.open('f_line.html')
