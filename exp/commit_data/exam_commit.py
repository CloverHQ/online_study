#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 12:26
# @Author  : liuwenchao
# @File    : exam_commit.py
# @Software: PyCharm


def commit_exam(session,course_id=None):
    exam_ids_url = 'http://www.wencaischool.com/openlearning/course/learning/learn_homework.jsp?course_id='+course_id
    exam_ids_text = session.get(exam_ids_url).text
    split_exam_id = exam_ids_text.split('ExamId=\\')
    for exam_id in range(1,len(split_exam_id)):
        print(str(exam_id) + '---------------------->'+split_exam_id[exam_id] )

