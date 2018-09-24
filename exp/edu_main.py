#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 11:36
# @Author  : liuwenchao
# @File    : edu_main.py
# @Software: PyCharm
from exp.common.edu_common import get_course_id
from exp.edu_online_study import commit_main


def common_main(session):
    # 获得course_id
    list = get_course_id(session)
    for i in range(len(list)):
        cus_id = list[i]['courseId']
        if cus_id == '':
            continue
        print(list[i]['courseName'] + '[数据提交中......]')
        main = commit_main(session,cus_id)
        main.commit_exam()
        main.commit_online_study()
        print(list[i]['courseName'] + '[提交完毕]')
