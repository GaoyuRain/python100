"""
author :admin
Date : 2021/08/03
Description : 爬虫
"""
import requests


def test01():
    cookies = {'key1': 'value1', 'key2': 'value2'}
    resp = requests.get('http://httpbin.org/cookies', cookies=cookies, proxies={})
    print(resp.text)

    jar = requests.cookies.RequestsCookieJar()
    pass
    # jar = requests.cookies.RequestsCookieJar()
