"""
author :rain
Date : 2021/03/16
Description :
"""
from pathlib import Path
import asyncio
import datetime
import re
import time
from datetime import datetime, timezone, timedelta
import aiohttp
import requests

requests.packages.urllib3.disable_warnings()

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    start = time.time()
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    endtime = time.time() - start
    print(endtime)
    loop.close()


def test01():
    urls = (
        'https://www.python.org/',
        'https://git-scm.com/',
        'https://www.jd.com/',
        'https://www.taobao.com/',
        'https://www.douban.com/',)
    start = time.time()
    for url in urls:
        # print(url)
        res = requests.get(url, verify=False, headers={'User-Agent': 'BaiduSpider'}).text
        # print(res)
        print(PATTERN.search(res).group('title'))
    endtime = time.time() - start
    print(endtime)


if __name__ == '__main__':
    # main()
    # test01()
    print(time.timezone)
    local_time_zone = (datetime.now() - datetime.utcnow()).seconds / 3600
    print("local_time_zone", local_time_zone)

