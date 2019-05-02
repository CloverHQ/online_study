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
user_config = {
    'student_num': '',
}

'''
    配置课程类型：
                other_course
                course
            
'''
type_config = {
    'course_type': 'other_course'
}

'''
配置参数:
        lesson_status是否完成 :
                        incompleted：未完成
                        completed ： 完成
        total_time总用时 ：建议使用60-70随机数
        score_max得分数：一般一节课分数为10
'''
lesson_config = {
    'less_status': lesson_status.completed.value,
    'score_max': '10',
    'total_time': random.randint(62, 70)
}

'''
    配置AES的key和iv向量
'''
encrypt_data_config = {
    'key': '',
    'iv': ''
}

exam_require_data = {
    'user_id': '',
    'user_school_code': '10466',
    'cur_grade_code': '20180',
}
