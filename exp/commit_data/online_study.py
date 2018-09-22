#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 10:20
# @Author  : liuwenchao
# @File    : online_study.py
# @Software: PyCharm

def commit_online_study(session,require_commit_data,txtCoursewareId,txtItemId):
    commit_url = 'http://www.wencaischool.com/openlearning_sync/servlet/com.lemon.web.ActionServlet?handler=com.lemon.scorm.ScormWebServlet&op=commit_data&script=&_no_html=0&0.1363493101209915'
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
                         'login_name'] + '&cmi.core.lesson_location=&cmi.core.credit=&cmi.core.lesson_status=incompleted&cmi.core.entry=&cmi.core.total_time=&cmi.core.lesson_mode=&cmi.core.exit=&cmi.core.session_time=11&cmi.core.score.raw=10&cmi.core.score.min=0&cmi.core.score.max=0&cmi.comments=&cmi.comments_from_lms=&cmi.launch_data=&cmi.student_data.mastery_score=0&cmi.student_data.max_time_allowed=0&cmi.student_data.time_limit_action=&cmi.student_preference.audio=0&cmi.student_preference.language=&cmi.student_preference.speed=0&cmi.student_preference.text=0&cmi.suspend_data=1&cmi.interactions.0.id=&cmi.interactions.0.time=60&cmi.interactions.0.type=content&cmi.interactions.0.weighting=0&cmi.interactions.0.student_response=&cmi.interactions.0.result=&cmi.interactions.0.latency=0',
        'txtCallBack': 'http://www.wencaischool.com/openlearning/scorm/scoplayer/after_commit.jsp?item_id=1999701&url=http%3a%2f%2fsource%2ewencaischool%2ecom%2fispace2%5fsync%2fscormplayer%2fcommit%2ehtm%3ftable%5findex%3d10466%5f20180%5f000279%260%2e6441710570737952'}
    session.post(url=commit_url, data=data)