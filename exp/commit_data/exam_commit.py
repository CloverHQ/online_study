#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 12:26
# @Author  : liuwenchao
# @File    : exam_commit.py
# @Software: PyCharm
import json

import requests

from exp.common.edu_common import exam_study
from exp.cryption.prpcrypt import prpcrypt

proxies = {
	"http" : "127.0.0.1:8080" # 代理ip
}

data = {

}

p = prpcrypt()

exam_data = {
    'exam_id':'4G+dyUAqycs/crL+5gdBqQ==',
    'course_code':'/ncH5eQsozFMnwXW8vbnPA==',
    'current_version':'NP+8bj8lCd3z8G0u4OZcGA==',
    'course_id':'O7yEER+HoF9gnCnfZGp2Dw==',
    'grade_code':'opn+imW9SwzspNlUQaX8rQ==',
    'app_release':'nOqVkA13Jv74+ugChBaZFg==',
    'exam_status':'P9UdazN874Ud/dXSFB15bA==',
    'phone_type':'mQ1mB1fHcgoWRJNXMOtUyw==',
    'school_code':'ClGZwbT7VpV/QiGkVZRmwQ==',
    'user_id':'U8HXCWeSqbEwFCsFmPPDNymbfaH7iHOaTLRvS0Am0KY=',
}

def commit_exam(session, cus_id=None):
    common_exam = exam_study(session, cus_id)
    ids = common_exam.get_ids()
    for id_index in range(1, len(ids)):
        exam_id = common_exam.get_exam_id(ids, id_index)
        exam_data['exam_id'] = p.encrypt(exam_id)
        exam_data['course_id'] = p.encrypt(cus_id)
        session.post(
            'http://www.wencaischool.com/openlearning/exam_and_task_list.action?req=getItemTypeTotalCount',
            exam_data)
        answers = json.loads(p.decrypt(session.post('http://www.wencaischool.com/openlearning/exam_and_task_list.action?req=getItemList',
                                   exam_data).json()['data']))['mallInfoList']
        for answer in answers:
            print(answer)
            da = answer['smallItemAnswer']
            for i in da:
                real_content = i['optionContent']
                real_key = i['myOptionKey']
                data[real_key] = real_content
        url = 'http://www.wencaischool.com/openlearning/servlet/com.lemon.web.ActionServlet?handler=com.lemon.learning.exam.StudentExamAction&op=submit_exam&exam_id='+exam_id+'&b_out=1&item_id=&_no_html=1&r=0.5873010551516843&88560'
        session.post(url,data)

if __name__ == '__main__':
    commit_exam(requests)