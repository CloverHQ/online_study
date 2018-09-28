#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 10:20
# @Author  : liuwenchao
# @File    : online_study_commit.py
# @Software: PyCharm

'''
    提交数据
'''

from exp.common.edu_common import *
from exp.config.config import lesson

less_status = lesson['less_status']
score_max = lesson['score_max']


commit_url = 'http://www.wencaischool.com/openlearning_sync/servlet/com.lemon.web.ActionServlet?handler=com.lemon.scorm.ScormWebServlet&op=commit_data&script=&_no_html=0&0.1363493101209915'

require_commit_data = {
        'user_id': '',
        'login_name': '',
        'user_school_code': '10466',
        'cur_grade_code': '20180',
        'cur_course_code': ''
    }


def commit_online_study(session, cus_id):
    common_tool = online_study(session, cus_id)
    content_ids = common_tool.get_content_ids()
    for id in range(len(content_ids)):
        content_id_meta = content_ids[id]
        content_id = common_tool.get_content_id(content_ids, id)
        folder_id = get_folder_id(content_ids, id)
        if '学习' not in content_id_meta or '完成学习' in content_id_meta:
            continue
        require_data = get_require_data(session, cus_id, content_id, folder_id)
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
                total_time = lesson['total_time']
                index = id.find('=')
                txtItemId = id[index + 2:index + 9]
                data = {
                'txtUserId': require_commit_data['user_id'],
                'txtSCOType': 'sco',
                'txtCoursewareId': txtCoursewareId,
                'txtItemId': txtItemId,
                'txtTableIndex': require_commit_data['user_school_code'] + '_' + require_commit_data[
                    'cur_grade_code'] + '_' + require_commit_data['cur_course_code'],
                # txtTableIndex可变  TODO 影响提交结果
                'txtCommit': 'cmi.core.student_id=' + require_commit_data[
                    'user_id'] + '&cmi.core.student_name=' + require_commit_data[
                                 'login_name'] + '&cmi.core.lesson_location=&cmi.core.credit=&cmi.core.lesson_status='+less_status+'&cmi.core.entry=&cmi.core.total_time='+str(total_time)+'&cmi.core.lesson_mode=&cmi.core.exit=&cmi.core.session_time=11&cmi.core.score.raw=10&cmi.core.score.min=0&cmi.core.score.max='+score_max+'&cmi.comments=&cmi.comments_from_lms=&cmi.launch_data=&cmi.student_data.mastery_score=0&cmi.student_data.max_time_allowed=0&cmi.student_data.time_limit_action=&cmi.student_preference.audio=0&cmi.student_preference.language=&cmi.student_preference.speed=0&cmi.student_preference.text=0&cmi.suspend_data=1&cmi.interactions.0.id=&cmi.interactions.0.time=60&cmi.interactions.0.type=content&cmi.interactions.0.weighting=0&cmi.interactions.0.student_response=&cmi.interactions.0.result=&cmi.interactions.0.latency=0',
                'txtCallBack': 'http://www.wencaischool.com/openlearning/scorm/scoplayer/after_commit.jsp?item_id=1999701&url=http%3a%2f%2fsource%2ewencaischool%2ecom%2fispace2%5fsync%2fscormplayer%2fcommit%2ehtm%3ftable%5findex%3d10466%5f20180%5f000279%260%2e6441710570737952'}
                #print(total_time)
                session.post(url=commit_url, data=data)
        break