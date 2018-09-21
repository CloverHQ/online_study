#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 10:42
# @Author  : liuwenchao
# @File    : edu_online_study.py
# @Software: PyCharm

from urllib import parse
import requests


'''
    在线学习提交数据
'''
def commit_online_study(session):
    require_commit_data = {
        'user_id': '',
        'login_name': '',
        'user_school_code': '10466',
        'cur_grade_code': '20180',
        'cur_course_code': ''
    }
    less_url = 'http://www.wencaischool.com/openlearning/console/course_list.jsp?0.4014251926637836'
    commit_url = 'http://www.wencaischool.com/openlearning_sync/servlet/com.lemon.web.ActionServlet?handler=com.lemon.scorm.ScormWebServlet&op=commit_data&script=&_no_html=0&0.1363493101209915'
    less_resp = session.get(url=less_url)
    data_json = less_resp.json()
    # 获取courseid
    list = data_json['other_course']
    for i in range(len(list)):
        cus_id = list[i]['courseId']
        if cus_id == '':
            continue
        print(list[i]['courseName'] + '[数据提交中......]')
        data = session.get(
            'http://www.wencaischool.com/openlearning/course/learning/learn_course.jsp?course_id=' + cus_id)
        html = data.text
        html_split = html.split('appendBlockHTML')
        content_ids = html_split[len(html_split) - 1].split('javascript:learnSco')
        txtCoursewareId = ''
        txtItemId = ''
        for id in range(len(content_ids)):
            content_id_meta = content_ids[id]
            folder_id = content_ids[id][26:33]
            content_id = content_ids[id][1:8]
            if '学习' not in content_id_meta or '完成学习' in content_id_meta:
                continue
            table_index = 'http://www.wencaischool.com/openlearning/scorm/scoplayer/?course_id=' + cus_id + '&content_id=' + content_id + '&urlto=index_sco.jsp?content_id=' + content_id + '&returl=../../course/learning/learn_course.jsp?course_id=' + cus_id + '&folder_id=' + folder_id + '&0.8562334125165616'
            table_index_resp = session.get(table_index)
            require_data = parse.unquote(requests.utils.unquote(table_index_resp.cookies['learning3_COOKIE'])).split(
                '&')
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
            item_url = ' http://www.wencaischool.com/openlearning/scorm/scoplayer/scorm_items_js.jsp?r=0.9314289966913749&course_id=' + cus_id + '&content_id=' + \
                       content_id + '&urlto=index_sco.jsp?content_id=' + content_id + '&returl=../../course/learning/learn_course.jsp?course_id=' + cus_id + '&folder_id=' + folder_id + '&0.9013073467077286&63050'
            item_id_html = session.get(url=item_url)
            item_ids = item_id_html.text.split('organHandle.')
            for item_id_index in range(len(item_ids)):
                id = item_ids[item_id_index]
                if 'coursewareId' in id:
                    txtCoursewareId = id[14:19]
                elif 'itemId' in id:
                    index = id.find('=')
                    txtItemId = id[index + 2:index + 9]
                    data = {
                        'txtUserId': require_commit_data['user_id'],
                        'txtSCOType': 'sco',
                        'txtCoursewareId': txtCoursewareId,
                        'txtItemId': txtItemId,
                        'txtTableIndex': require_commit_data['user_school_code']+'_'+require_commit_data['cur_grade_code']+'_'+ require_commit_data['cur_course_code'],  # txtTableIndex可变  TODO 影响提交结果
                        'txtCommit': 'cmi.core.student_id=' + require_commit_data[
                            'user_id'] + '&cmi.core.student_name=' + require_commit_data[
                                         'login_name'] + '&cmi.core.lesson_location=&cmi.core.credit=&cmi.core.lesson_status=incompleted&cmi.core.entry=&cmi.core.total_time=&cmi.core.lesson_mode=&cmi.core.exit=&cmi.core.session_time=11&cmi.core.score.raw=10&cmi.core.score.min=0&cmi.core.score.max=0&cmi.comments=&cmi.comments_from_lms=&cmi.launch_data=&cmi.student_data.mastery_score=0&cmi.student_data.max_time_allowed=0&cmi.student_data.time_limit_action=&cmi.student_preference.audio=0&cmi.student_preference.language=&cmi.student_preference.speed=0&cmi.student_preference.text=0&cmi.suspend_data=1&cmi.interactions.0.id=&cmi.interactions.0.time=60&cmi.interactions.0.type=content&cmi.interactions.0.weighting=0&cmi.interactions.0.student_response=&cmi.interactions.0.result=&cmi.interactions.0.latency=0',
                        'txtCallBack': 'http://www.wencaischool.com/openlearning/scorm/scoplayer/after_commit.jsp?item_id=1999701&url=http%3a%2f%2fsource%2ewencaischool%2ecom%2fispace2%5fsync%2fscormplayer%2fcommit%2ehtm%3ftable%5findex%3d10466%5f20180%5f000279%260%2e6441710570737952'}
                    session.post(url=commit_url, data=data)
            break
        print(list[i]['courseName']+'[提交完毕]')
