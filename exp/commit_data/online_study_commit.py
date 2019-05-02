#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 10:20
# @Author  : liuwenchao
# @File    : online_study_commit.py
# @Software: PyCharm

'''
    提交数据
'''
from urllib.parse import unquote, urlencode

from exp.config.config import lesson_config as lesson, lesson_config
from exp.cryption.prpcrypt import prpcrypt

less_status = lesson['less_status']
score_max = lesson['score_max']


commit_url = 'http://www.wencaischool.com/openlearning/learning.action?req=submitScorm'
len_url = 'http://www.wencaischool.com/openlearning/Scorm.action?req=getCourseScormItemDetail'
url = 'http://www.wencaischool.com/openlearning/Scorm.action?req=getCourseScormItemList'
history_url = 'http://www.wencaischool.com/openlearning/user_scorm_history_save.action'

p = prpcrypt()

def encrypt(str):
    return p.encrypt(str)


def decrypt(str):
    return p.decrypt(str)


require_commit_data = {
        'user_id': '',
        'login_name': '',
        'user_school_code': '10466',
        'cur_grade_code': '20180',
        'cur_course_code': ''
    }

def commit_online_study(session, cus_id):
    item_id_data = {
        'course_id': encrypt(cus_id)
    }

    len = {
        'course_id': encrypt(cus_id),
        'scorm_item_id': ''
    }

    history_data = {
        'course_id': encrypt(cus_id),
        'learning_user_id':encrypt(unquote(session.cookies['learning3_COOKIE']).split('&')[1].split('=')[1]),
        'scorm_id':'',
        'view_time':''
    }

    data = {
        'course_id': encrypt(cus_id),
        'user_id': encrypt(unquote(session.cookies['learning3_COOKIE']).split('&')[1].split('=')[1]),
        'item_id': '',
        'time': '',
        'video_length':''
    }
    resp = session.post(url, data=item_id_data).json()
    debug_date = resp['debugData']
    for debug in debug_date:
        scorm_items = debug['listScormItem']
        for item in scorm_items :
            if item['isFinish']:
                continue
            header = {
                'Referer': 'http://www.wencaischool.com/openlearning/separation/courseware/index.html?course_id=' + cus_id + '&school_code=10466&grade_code=20180&scorm_item_id='+item['itemId']+'5&user_id=_learning3_159726&returl=',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
            }
            data['item_id'] = encrypt(item['itemId'])
            len['scorm_item_id'] = encrypt(item['itemId'])
            print(lesson_config['total_time'])
            data['time'] = encrypt(str(lesson_config['total_time']))
            len_ = session.post(url=len_url, data=len).json()['debugData']['timeLen']
            data['video_length'] = encrypt(str(len_))
            history_data['scorm_id'] = encrypt(item['itemId'])
            history_data['view_time'] = encrypt(str(lesson_config['total_time']))
            session.post(url=history_url,data=history_data, headers = header)
            print(urlencode(data))
            print(session.post(url=commit_url, data=data, headers=header).json())
