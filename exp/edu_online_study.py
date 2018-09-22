#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 10:42
# @Author  : liuwenchao
# @File    : edu_online_study.py
# @Software: PyCharm

from exp.commit_data.exam_commit import commit_exam
from exp.commit_data.online_study_commit import commit_online_study
from exp.common.edu_common import *

'''
    在线学习提交数据
'''


def common_main(session):
    # 获得course_id
    list = get_course_id(session)
    for i in range(len(list)):
        cus_id = list[i]['courseId']
        if cus_id == '':
            continue
        print(list[i]['courseName'] + '[数据提交中......]')
        commit_exam(session, cus_id)
        commit_online_study(session, cus_id)
        print(list[i]['courseName'] + '[提交完毕]')
