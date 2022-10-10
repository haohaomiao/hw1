# -*- coding: utf-8 -*-
# from nis import match
import re
def register_params_check(content):
    """
    TODO: 进行参数检查
    """
    # 检查username
    username = content.get('username')
    if username is None:
        return "username",False
    elif (re.search('^[A-Za-z]+[0-9]+$',username) is None) or (re.search('^.{5,12}$',username) is None):
        return "username",False
    # 检查password
    password = content.get('password')
    if password is None:
        return "password",False
    elif((re.search('^[A-Za-z0-9\-\_\*\.]{8,15}$',password) is None)  or 
        (re.search('[A-Z]',password) is None) or 
        (re.search('[a-z]',password) is None) or 
        (re.search('[0-9]',password) is None) or
        (re.search('[\-\_\*\.]',password) is None)
        ):
        return "password",False
    # 检查nickname
    nickname = content.get('nickname')
    if nickname is None or nickname == '':
        return "nickname",False
    # 检查url
    url = content.get('url')
    if url is None:
        return "url",False
    elif((re.search('https?://([A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]\.)+[0-9A-Za-z]+',url) is None) or 
        (re.search('\.[^0-9]+$',url) is None) or
        (re.search('^.{,48}$',url) is None)):
        return "url",False
    # 检查mobile
    mobile = content.get('mobile')
    if mobile is None:
        return "mobile",False
    elif((re.search('^\+[0-9]{2}\.[0-9]{12}$',mobile) is None)):
        return "mobile",False
    # 检查magic_number
    magic_number = content.get('magic_number')
    if magic_number is None or magic_number == "":
        content['magic_number'] = 0
    elif re.search('^[0-9]+$',magic_number) is None:
        return "magic_number",False
    return "ok", True
