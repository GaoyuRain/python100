"""
author :rain
Date : 2020/09/04
Description :
"""
import json
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
import requests


def test1():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'gaoyu_rain@163.com'
    receivers = ['gaoyu_rain@163.com']
    message = MIMEText('hi.rain', 'plain', 'utf-8')
    message['From'] = Header('rain', 'utf-8')
    message['To'] = Header('高雨', 'utf-8')
    message['Subject'] = Header('你在哪呢', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'IDSJKAPOSUEWBHWC')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


def test2():
    url = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
    params = {'': '', 'account': 'C99831141', 'password': 'd483ed9e72df33222f4f71d956680d59', 'mobile': '17612136829',
              'content': '测试短信', 'format': 'json'}
    r = requests.get(url, params=params)
    print(r)
    print(r.content)
    print(r.text)
    print(r.json())


if __name__ == '__main__':
    test2()
