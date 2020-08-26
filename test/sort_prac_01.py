"""
author :Rain
Date : 2019/08/16
Description :排序算法练习
"""
import random


def test01():
    # data = [1, 2, 3, 4]
    data = []
    for i in range(21):
        data.append(random.randint(1,21))

    print(data)
    # 交换次数
    num = 0
    for i in range(len(data) - 1):
        exchange = False
        for n in range(len(data) - 1):
            if data[n] > data[n + 1]:
                data[n + 1], data[n] = data[n], data[n + 1]
                exchange = True
                num += 1
        if not exchange:
            print('排序结束，交换次数:', num)
            break

    print(data)


if __name__ == '__main__':
    test01()
