#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 12:26
# @Author  : liuwenchao
# @File    : exam_commit.py
# @Software: PyCharm
from builtins import print
from time import sleep

import requests
from selenium import webdriver

from exp.common.edu_common import exam_study

chrome = webdriver.Chrome()
chrome.get('http://www.wencaischool.com/')



def commit_exam(session, cus_id=None):
    common_exam = exam_study(session, cus_id)
    ids = common_exam.get_ids()
    login_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    chrome.add_cookie({'name': 'learning3_COOKIE', 'value': login_cookie['learning3_COOKIE']})
    for id_index in range(1, len(ids)):
        content_id = common_exam.get_content_id(ids, id_index)
        exam_id = common_exam.get_exam_id(ids, id_index)
        score_ids = common_exam.get_score_ids(exam_id, content_id)
        score_id_split = score_ids.split('score_id=')
        print(exam_id)
        for score_index in range(1, len(score_id_split)):
            score_id = score_id_split[score_index][0:6]
            try:
                int(score_id)
            except Exception as e:
                print(e)
            chrome.get(
                'http://www.wencaischool.com/openlearning/console/?urlto=http://www.wencaischool.com/openlearning/course/learning/learn_course.jsp?course_id=' + cus_id + '&0.33649536487019127')
            sleep(3)
            chrome.switch_to.frame('w_main')
            course_menu = chrome.find_element_by_css_selector('.course_menu ul')
            course_menu.find_element_by_link_text('作业和测验').click()
            sleep(10)
            # data = chrome.get('http://www.wencaischool.com/openlearning/exam/portal/view_answer.jsp?exam_id='+exam_id+'&score_id='+score_id+'&exam_id='+exam_id+'&type=work&content_id='+content_id+'&type=work&is_make_up=undefined&reexamine=0&94302')
            # print(data)
            # chrome.quit()
