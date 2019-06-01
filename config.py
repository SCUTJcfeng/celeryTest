# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: celeryTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-01 10:36:33
Last Modified: 2019-06-01 10:38:03
'''

broker_url = 'redis://127.0.0.1:6380/5'
result_backend = 'redis://127.0.0.1:6380/6'

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True
