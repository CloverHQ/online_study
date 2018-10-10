#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 14:17
# @Author  : liuwenchao
# @File    : edu_common.py
# @Software: PyCharm
from urllib import parse
import requests

from exp.common.common_interface import common_tool
from exp.config.config import type_config


class online_study(common_tool):

    def get_content_ids(self):
        data = self.session.get(
            'http://www.wencaischool.com/openlearning/course/learning/learn_course.jsp?course_id=' + self.cus_id)
        html = data.text
        html_split = html.split('appendBlockHTML')
        content_ids = html_split[len(html_split) - 1].split('javascript:learnSco')
        return content_ids

    def get_content_id(self, content_ids, id):
        content_id = content_ids[id][1:8]
        return content_id


class exam_study(common_tool):
    def __init__(self, session, cus_id):
        super().__init__(session, cus_id)
        self.text = self.session.get(
            'http://www.wencaischool.com/openlearning/course/learning/learn_homework.jsp?course_id=' + self.cus_id).text
        self.ids = self.text.split('ExamId=\\')

    def get_ids(self):
        return self.ids

    def get_content_id(self, content_ids, index):
        return content_ids[index][21:28]

    def get_exam_id(self, exam_ids, index):
        return exam_ids[index][1:6]

    def get_score_ids(self, exam_id, content_id):
        score_id_resp = self.session.get(
            'http://www.wencaischool.com/openlearning/exam/portal/exam_info.jsp?exam_id='+exam_id+'&type=work&content_id='+content_id+'&type=work&is_make_up=undefined').text
        return score_id_resp

def get_folder_id(content_ids, id):
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
    list = data_json[type_config['course_type']]
    return list
