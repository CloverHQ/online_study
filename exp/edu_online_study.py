#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 10:42
# @Author  : liuwenchao
# @File    : edu_online_study.py
# @Software: PyCharm

from exp.commit_data.exam_commit import commit_exam
from exp.commit_data.online_study_commit import commit_online_study

'''
    提交数据
'''


class commit_main():
    def __init__(self, session, cus_id):
        self.session = session
        self.cus_id = cus_id

    def commit_exam(self):
        return commit_exam(self.session, self.cus_id)

    def commit_online_study(self):
        return commit_online_study(self.session, self.cus_id)

