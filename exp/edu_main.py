#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 11:36
# @Author  : liuwenchao
# @File    : edu_main.py
# @Software: PyCharm
from urllib.parse import unquote

from exp.common.edu_common import get_course_id
from exp.config.config import exam_require_data
from exp.cryption.prpcrypt import prpcrypt
from exp.edu_online_study import commit_main


def common_main(session):
    # 获得course_id
    exam_require_data['user_id'] = prpcrypt().encrypt(unquote(session.cookies['openlearning_COOKIE']).split('&')[1].split('=')[1])
    list = get_course_id(session)
    for i in range(len(list)):
        cus_id = list[i]['courseId']
        if cus_id == '':
            continue
        print(list[i]['courseName'] + '[数据提交中......]')
        main = commit_main(session,cus_id)
        #main.commit_online_study()
        main.commit_exam()
        print(list[i]['courseName'] + '[提交完毕]')
