"""
author :rain
Date : 2020/09/03
Description :
"""
from multiprocessing import Process, Queue
from time import sleep

counter = 0

q = Queue(maxsize=0)


def sub_task(data):
    global counter
    while counter < 5:
        print(data)
        counter += 1
        sleep(0.01)


def sub_task1(data):
    count = 0
    q.put(count)
    while count < 5:
        print(data)
        count = q.get()
        count += 1
        sleep(0.01)
    q.task_done()


def main():
    # count_queen = queues.SimpleQueue()
    # count_queen.numerator = 0
    p1 = Process(target=sub_task, args=('ping',))
    p2 = Process(target=sub_task, args=('pong',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('-' * 50)

    # TODO 有问题代码
    Process(target=sub_task1, args=('ping',)).start()
    Process(target=sub_task1, args=('pong',)).start()


if __name__ == '__main__':
    main()
