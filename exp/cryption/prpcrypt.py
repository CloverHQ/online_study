#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 14:22
# @Author  : liuwenchao
# @File    : prpcrypt.py
# @Software: PyCharm

from Crypto.Cipher import AES
import base64

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

    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        text = pad(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        cipher_text = cryptor.encrypt(text.encode('utf-8'))
        return base64.standard_b64encode(cipher_text).decode("utf-8")

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        de_text = base64.standard_b64decode(text)
        plain_text = cryptor.decrypt(de_text)
        st = str(plain_text.decode("utf-8")).rstrip('\0')
        out = unpad(st)
        return out
