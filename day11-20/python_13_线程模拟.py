# 模拟计算密集型任务
from multiprocessing import Process, Queue
from random import randint
from time import time
import requests


def task_handler(cur_list, result_queue):
    total = 0
    for num in cur_list:
        total += num
    result_queue.put(total)


def main():
    s = time()
    processs = []
    total_list = [x for x in range(1, 40000001)]
    result_queue = Queue()
    # 启动八个进程，将数据切片后运算
    e1 = time()
    print("%.3f" % (e1 - s))
    index = 0
    for _ in range(8):
        p = Process(target=task_handler, args=(total_list[index:index + 5000000], result_queue))
        index += 5000000
        processs.append(p)
        p.start()
    e = time()
    print('数据准备耗时：%.3f' % (e - s))
    # 开始记录所有进程所需的时间
    start = time()
    for p in processs:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print('total:', total)
    end = time()
    print('数据计算耗时：%.3f' % (end - start))


if __name__ == '__main__':
    main()
