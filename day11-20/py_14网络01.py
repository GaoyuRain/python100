# 模拟计算密集型任务
from multiprocessing import Process, Queue
from random import randint
from threading import Thread
from time import time
import requests


class DownLoadThread(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        data = requests.get(self.url)
        with open('./pic/' + filename, 'wb') as file:
            file.write(data.content)


def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=dfc292c3becf2c5198d4fd1d2499c100&num=10')
    data_modal = resp.json()
    for mm_dict in data_modal['newslist']:
        url = mm_dict['picUrl']
        DownLoadThread(url).start()


if __name__ == '__main__':
    main()
