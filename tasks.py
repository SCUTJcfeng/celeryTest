# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: celeryTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-05-31 15:09:23
Last Modified: 2019-05-31 15:18:59
'''

from celery import Celery

broker = 'redis://127.0.0.1:6380/5'
backend = 'redis://127.0.0.1:6380/6'

app = Celery('tasks', broker=broker, backend=backend)


@app.task
def add(x, y):
    return x + y
