# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: celeryTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-05-31 15:28:02
Last Modified: 2019-05-31 16:21:34
'''

from tasks import add


res = add.delay(4, 4)
while True:
    if res.ready():
        break
print(f'state: {res.state} result: {res.get()}')
