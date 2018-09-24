#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 15:52
# @Author  : liuwenchao
# @File    : lesson_status.py
# @Software: PyCharm

from enum import Enum


class lesson_status(Enum):
    incompleted = 'incompleted'
    completed = 'completed'