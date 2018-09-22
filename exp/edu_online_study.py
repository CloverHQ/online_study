#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 10:42
# @Author  : liuwenchao
# @File    : edu_online_study.py
# @Software: PyCharm

from urllib import parse
import requests

from exp.common.edu_common import get_course_id, get_content_id, get_folder_id, get_content_ids, get_require_data, \
     get_item_ids

from exp.commit_data.online_study import commit_online_study
'''
    在线学习提交数据
'''


def common_main(session):
    require_commit_data = {
        'user_id': '',
        'login_name': '',
        'user_school_code': '10466',
        'cur_grade_code': '20180',
        'cur_course_code': ''
    }

    # 获得course_id
    list = get_course_id(session)
    for i in range(len(list)):
        cus_id = list[i]['courseId']
        if cus_id == '':
            continue
        print(list[i]['courseName'] + '[数据提交中......]')
        content_ids = get_content_ids(session, cus_id)
        for id in range(len(content_ids)):
            content_id_meta = content_ids[id]
            content_id = get_content_id(content_ids,id)
            folder_id = get_folder_id(content_ids,id)
            if '学习' not in content_id_meta:
                continue
            require_data = get_require_data(session, cus_id, content_id,folder_id)
            for rd in range(len(require_data)):
                require_data_i_ = require_data[rd]
                if 'user_id' in require_data_i_:
                    require_commit_data['user_id'] = require_data_i_.split('=')[1]
                if 'login_name' in require_data_i_:
                    require_commit_data['login_name'] = require_data_i_.split('=')[1]
                if 'user_school_code' in require_data_i_:
                    require_commit_data['user_school_code'] = require_data_i_.split('=')[1]
                if 'cur_course_code' in require_data_i_:
                    require_commit_data['cur_course_code'] = require_data_i_.split('=')[1]
                if 'cur_grade_code' in require_data_i_:
                    require_commit_data['cur_grade_code'] = require_data_i_.split('=')[1]
            item_ids = get_item_ids(session, cus_id, content_id, folder_id)
            txtCoursewareId = ''
            for item_id_index in range(len(item_ids)):
                id = item_ids[item_id_index]
                if 'coursewareId' in id:
                    txtCoursewareId = id[14:19]
                elif 'itemId' in id:
                    index = id.find('=')
                    txtItemId = id[index + 2:index + 9]
                    commit_online_study(session,require_commit_data,txtCoursewareId,txtItemId)
            break
        print(list[i]['courseName'] + '[提交完毕]')
