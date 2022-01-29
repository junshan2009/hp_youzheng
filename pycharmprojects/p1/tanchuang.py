# !/usr/bin/env python
# -*-coding:utf-8 -*-

from plyer import notification

notification.notify(
    title="内网登录提醒",
    message="不在时间范围内",
    timeout=5
)
