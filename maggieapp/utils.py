import json
import re
import random
from hashlib import md5

import requests
from django.core.cache import caches
from django.core.mail import send_mail
from django.shortcuts import render
from django.template import loader

from PetHome import app, settings

USERNAME_PATTERN = re.compile(r'^\w{6,20}$')
PASSWORD_PATTERN = re.compile(r'^\w{8,20}$')
TEL_PATTERN = re.compile(r'1[3-9]\d{9}')
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')


def normalize_space(usernameandpassword):
    """去空格"""
    return usernameandpassword.replace(' ', '')


def gen_email_code(length=4):
    """生成指定长度的手机验证码"""
    return ''.join(random.choices('0123456789', k=length))


def send_sms_by_luosimao(tel, message):
    """发送短信（调用螺丝帽短信网关）"""
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-50ba1f06ff0621d335b777a4edd1c0ff'),
        data={
            'mobile': tel,
            'message': message
        },
        timeout=10,
        verify=False)
    return json.loads(resp.content)


def to_md5_hex(origin_str):
    """生成MD5摘要"""
    return md5(origin_str.encode('utf-8')).hexdigest()


@app.task()
def send_active_email(email, email_code):
    title = '宠物圈验证码'
    msg = '异步操作'
    sender = settings.DEFAULT_FROM_EMAIL
    reciever = email
    tmp = loader.get_template('email_temp.html')
    html_str = tmp.render({'code': email_code})
    send_mail(title, msg, sender, reciever, html_message=html_str)
