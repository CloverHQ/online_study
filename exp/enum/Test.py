#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 22:33
# @Author  : liuwenchao
# @File    : Test.py
# @Software: PyCharm

import requests



if __name__ == '__main__':
    print(requests.session().get('http://www.baidu.com'))