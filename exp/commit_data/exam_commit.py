#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 12:26
# @Author  : liuwenchao
# @File    : exam_commit.py
# @Software: PyCharm
from urllib import parse

import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from exp.common.edu_common import exam_study

chrome = webdriver.Chrome()
chrome.get('http://www.wencaischool.com/')
# chrome.fullscreen_window()

proxies = {
	"http" : "127.0.0.1:8080" # 代理ip
}

data = {

}


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
        for score_index in range(1, len(score_id_split)):
            score_id = score_id_split[score_index][0:6]
            chrome.get(
                'http://www.wencaischool.com/openlearning/console/?urlto=http://www.wencaischool.com/openlearning/course/learning/learn_course.jsp?course_id=' + cus_id + '&0.33649536487019127')
            sleep(3)
            chrome.switch_to.frame('w_main')
            chrome.find_element_by_css_selector('.course_menu ul').find_element_by_link_text('作业和测验').click()
            join_exam = chrome.find_elements(By.CLASS_NAME, 'func_narrow')
            for je_id in range(len(join_exam)):
                sleep(3)
                join_exam[je_id].click()
                sleep(10)
                print(chrome.find_element_by_id('cboxIframe').get_attribute('id'))
                chrome.switch_to.frame('cboxIframe')
                chrome.switch_to.frame('w_lms_content')
                chrome.switch_to.frame('w_lms_sco')
                start_exam = chrome.find_element(By.ID, 'btnExam')
                value = start_exam.get_attribute('value')
                if '重考' in value:
                    chrome.find_element_by_class_name('btn90').click()
                    form_ids = chrome.find_elements(By.XPATH, '//input[starts-with(@name,\'lemonysoft_item_\')]')
                    temp_name = []
                    [temp_name.append(form_ids[i].get_attribute('name')) for i in range(len(form_ids)) if
                     form_ids[i].get_attribute('name') not in temp_name]
                    answers = chrome.find_elements(By.XPATH, '//*[contains(text(),\'参考答案\')]')
                    temp_answer = []
                    [temp_answer.append(i) for i in answers if '参考答案' in i.text]
                    for temp_id in range(len(temp_name)):
                        answer_text = temp_answer[temp_id].text
                        data[temp_name[temp_id]] = answer_text[answer_text.index('案：')+2:answer_text.rfind(']')]
                    session.post(
                        'http://www.wencaischool.com/openlearning/servlet/com.lemon.web.ActionServlet?handler=com%2elemon%2elearning%2eexam%2eStudentExamAction&op=submit_exam&exam_id=' + exam_id + '&b_out=1&item_id=&_no_html=1&r=0%2e598268127988989&41836',
                        data=data, proxies=proxies)
                    chrome.switch_to.parent_frame()
                    chrome.switch_to.parent_frame()
                    chrome.switch_to.parent_frame()
                else:
                    start_exam.click()
                print(value)
                sleep(10)
            try:
                int(score_id)
            except Exception as e:
                print(e)

