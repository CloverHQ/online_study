#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 23:54
# @Author  : liuwenchao
# @File    : config.py
# @Software: PyCharm
import random

from exp.lesson_enum.lesson_status import lesson_status

'''
    学号设置
'''
user = {
    'student_num': '',
}

'''
配置参数:
        lesson_status是否完成 :
                        incompleted：未完成
                        completed ： 完成
        total_time总用时 ：建议使用60-70随机数
        score_max得分数：一般一节课分数为10
'''
lesson = {
    'less_status': lesson_status.completed.value,
    'score_max': '10',
    'total_time': random.randint(62, 70)
}

encrypt_data = {
    'key':'',
    'iv':''
}
