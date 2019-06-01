# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: celeryTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-05-31 15:09:23
Last Modified: 2019-06-01 10:37:08
'''

from celery import Celery


app = Celery('tasks')
app.config_from_object('config')


@app.task
def add(x, y):
    return x + y
