# !/usr/bin/env python
# -*-coding:utf-8 -*-

import PySimpleGUI as sg

layout = [
    [sg.Text('一句话概括Python')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('确认'), sg.Button('取消')]
]
window = sg.Window('PySimpleGUI Demo', layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event in (None, '取消'):
        break
window.close()