#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:22
# @Author  : liuwenchao
# @File    : prpcrypt.py
# @Software: PyCharm
import requests
from Crypto.Cipher import AES
import base64

from exp.config.config import encrypt_data

BS = AES.block_size

'''
    处理加密数据
'''


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


# 定义 padding 即 填充 为PKCS7
def unpad(s):
    return s[0:-ord(s[-1])]


class prpcrypt(object):

    def __init__(self):
        self.key = encrypt_data['key'].encode('utf-8')
        self.iv = encrypt_data['iv'].encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        text = pad(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        cipher_text = cryptor.encrypt(text.encode('utf-8'))
        return base64.standard_b64encode(cipher_text).decode("utf-8")

    def decrypt(self, text):
        text = pad(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        de_text = base64.standard_b64decode(text)
        plain_text = cryptor.decrypt(de_text)
        st = str(plain_text.decode("utf-8")).rstrip('\0')
        out = unpad(st)
        return out

data ={
    'status':'P9UdazN874Ud/dXSFB15bA==',
    'current_version':'NP+8bj8lCd3z8G0u4OZcGA==',
    'course_id':'se1NynsDAbCPnjewcAtp2w==',
    'grade_code':'opn+imW9SwzspNlUQaX8rQ==',
    'app_release':'nOqVkA13Jv74+ugChBaZFg==',
    'phone_type':'mQ1mB1fHcgoWRJNXMOtUyw==',
    'school_code':'ClGZwbT7VpV/QiGkVZRmwQ==',
    'user_id':'U8HXCWeSqbEwFCsFmPPDNymbfaH7iHOaTLRvS0Am0KY='
}

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

if __name__ == '__main__':
    print(requests.post('http://www.wencaischool.com/openlearning/get_exercise_list.action?', data).json())

    key = '5165325946459632'  # key
    iv = '8655624543959233'  # iv向量
    p = prpcrypt(key=key, iv=iv)
    for i in exam_data.values():
        print(p.decrypt(i))
    print(p.encrypt('76601'))
    print(requests.post('http://www.wencaischool.com/openlearning/exam_and_task_list.action?req=getItemTypeTotalCount',
                        exam_data).json())
    print(requests.post('http://www.wencaischool.com/openlearning/exam_and_task_list.action?req=getItemList',
                        exam_data).json())
