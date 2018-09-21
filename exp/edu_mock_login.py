#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 9:17
# @Author  : liuwenchao
# @File    : edu_mock_login.py
# @Software: PyCharm

import requests
import json
from urllib import parse

from exp.cryption.prpcrypt import prpcrypt
from exp.edu_online_study import commit_online_study

'''
    模拟登陆
'''

def mockLogin(userName, passWord='123456'):
    login_url = 'http://crjy.wencaischool.com/hnnydx/servlet/com.lemon.web.ActionServlet?handler=com.ifree.system.user.UserLoginAction&op=login&_no_html=1&0.15718558890528422'
    get_cookie_url = 'http://crjy.wencaischool.com//hnnydx_student/login.jsp?txtLoginName=' + userName + '&txtPassword=' + passWord + '&ran=0.7865230691042007&96685'

    data = {
        'txtLoginName': userName,
        'txtPassword': passWord
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer': 'http://source.wencaischool.com/ispace2_sync/scormplayer/commit.htm?table_index=10466_20180_000279&0.9413105898484105',
        'Cookie': ''
    }

    session = requests.Session()
    session.headers = header
    session.post(url=login_url, data=data)
    cookie_resp = session.get(get_cookie_url)
    session.headers = cookie_resp.request.headers
    # 课程获取cus_id
    get_term = 'http://crjy.wencaischool.com/hnnydx_student/student_learn.action?req=getTerm'
    less_data = {
        'term_code': ''
    }
    less_url = 'http://crjy.wencaischool.com/hnnydx_student/student_learn.action?req=getStudentLearnInfo'
    term_resp = session.get(get_term)
    term_list = json.loads(decrypt(term_resp.json()['data']))
    for term_index in range(len(term_list)):
        term = term_list[term_index]
        if term['isCurrentTerm']:
            less_data['term_code'] = term['termCode']
    # 获得课程列表
    less_resp = session.post(less_url, data=encrypt(less_data['term_code']))
    less_json = json.loads(decrypt(less_resp.json()['data']))
    less_list = less_json['courseInfoList']

    study_online_url = 'http://www.wencaischool.com/openlearning/login.jsp?op=execscript&ip_exp_prefix=@@IPEXP_&ip_replace_exp=http://125.70.12.165:8000/openlearning_uploadSCORM_UPLOAD_WEBhttp://www.wencaischool.com/openlearningLEARNING_WEBhttp://www.wencaischool.com/files/learning3FILES_WEB_UPLOAD_FOLDERhttp://www.wencaischool.com/filesFILES_WEB&59089'
    study_online_data = {
        'txtGradeCode': '',
        'txtLoginName': '',
        'txtPassword': '',
        'txtSchoolCode': ''
    }
    # 获取登陆cookie
    less = less_list[0]
    result = parse.urlparse(less['filePath'])
    # 格式化url
    parse_parse_qs = parse.parse_qs(result.query)
    study_online_data['txtPassword'] = parse_parse_qs['password'][0]
    study_online_data['txtGradeCode'] = parse_parse_qs['grade_code'][0]
    study_online_data['txtLoginName'] = 'hnnydx_' + parse_parse_qs['login_name'][0]
    study_online_data['txtSchoolCode'] = parse_parse_qs['school_code'][0]
    set_cookies = session.post(study_online_url, data=study_online_data)
    header = requests.utils.dict_from_cookiejar(set_cookies.cookies)
    session.headers = header
    return session


key = '5165325946459632'  # key
iv = '8655624543959233'  # iv向量
p = prpcrypt(key=key, iv=iv)


def encrypt(str):
    return p.encrypt(str)


def decrypt(str):
    return p.decrypt(str)



if __name__ == '__main__':
    # 获取登陆状态
    session = mockLogin('输入学号')
    commit_online_study(session)
