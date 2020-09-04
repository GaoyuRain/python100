# 模拟计算密集型任务
from multiprocessing import Process, Queue
from random import randint
from time import time
import requests


def test1():
    total = 0
    # 切片操作也很费时间
    start1 = time()
    num_list = [x for x in range(1, 100000001)]
    start2 = time()
    for i in num_list:
        total += i
    end = time()

    print('test1-1 耗时%.2f s' % (end - start1))
    print('test1-2 耗时%.2f s' % (end - start2))


def task_handler(cur_list, result_queue):
    total = 0
    for num in cur_list:
        total += num
    result_queue.put(total)


def test2():
    process = []
    total = 0
    result_quene = Queue()
    start1 = time()
    num_list = [x for x in range(1, 100000001)]
    num_list1 = []
    index = 0
    start2 = time()
    # 启动八个进程，将数据切片后运算
    for i in range(8):
        nl = num_list[index:index + 12500000]
        num_list1.append(nl)
        index += 12500000
    start3 = time()
    for i in num_list1:
        p = Process(target=task_handler, args=(i, result_quene))
        process.append(p)
        p.start()
    for p in process:
        p.join()
    while not result_quene.empty():
        total += result_quene.get()
    end = time()
    print('test2-1 耗时%.2f s' % (end - start1))
    print('test2-2 耗时%.2f s' % (end - start2))
    print('test2-3 耗时%.2f s' % (end - start3))
    print(total)


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
    # main()
    test1()
    print('-' * 50)
    test2()
