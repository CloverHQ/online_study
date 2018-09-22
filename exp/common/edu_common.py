#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 14:17
# @Author  : liuwenchao
# @File    : edu_common.py
# @Software: PyCharm
from urllib import parse
import requests

course_type = 'other_course'


def get_content_ids(session, cus_id):
    data = session.get(
        'http://www.wencaischool.com/openlearning/course/learning/learn_course.jsp?course_id=' + cus_id)
    html = data.text
    html_split = html.split('appendBlockHTML')
    content_ids = html_split[len(html_split) - 1].split('javascript:learnSco')
    return content_ids


def get_content_id(content_ids,id):
    content_id = content_ids[id][1:8]
    return content_id


def get_folder_id(content_ids,id):
    return content_ids[id][26:33]


def get_item_ids(session, cus_id, content_id, folder_id):
    item_url = ' http://www.wencaischool.com/openlearning/scorm/scoplayer/scorm_items_js.jsp?r=0.9314289966913749&course_id=' + cus_id + '&content_id=' + \
               content_id + '&urlto=index_sco.jsp?content_id=' + content_id + '&returl=../../course/learning/learn_course.jsp?course_id=' + cus_id + '&folder_id=' + folder_id + '&0.9013073467077286&63050'
    item_id_html = session.get(url=item_url)
    item_ids = item_id_html.text.split('organHandle.')
    return item_ids

def get_item_id():
    pass

def get_require_data(session, cus_id, content_id, folder_id):
    table_index = 'http://www.wencaischool.com/openlearning/scorm/scoplayer/?course_id=' + cus_id + '&content_id=' + content_id + '&urlto=index_sco.jsp?content_id=' + content_id + '&returl=../../course/learning/learn_course.jsp?course_id=' + cus_id + '&folder_id=' + folder_id + '&0.8562334125165616'
    table_index_resp = session.get(table_index)
    require_data = parse.unquote(requests.utils.unquote(table_index_resp.cookies['learning3_COOKIE'])).split(
        '&')
    return require_data


def get_course_id(session):
    less_url = 'http://www.wencaischool.com/openlearning/console/course_list.jsp?0.4014251926637836'
    less_resp = session.get(url=less_url)
    data_json = less_resp.json()
    list = data_json[course_type]
    return list
