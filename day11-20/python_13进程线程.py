import time
from threading import Thread, Lock


class Account(object):
    def __init__(self, name):
        self._balance = 0
        self._lock = Lock()
        self.name = name

    def deposit(self, money):
        # 线程 获取锁 不允许其他线程进入
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            # 模拟操作数据的耗时
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            pass
            # 释放锁
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account('rain')
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(account.name + ' 余额:', account.balance)


def test():
    A = [1, 3, 2,3]
    for i in range(len(A) - 1):
        print(A[i])
        if A[i] != i:
            if A[i] == A[A[i]]:
                print('有重复元素：', A[i])
                break
    else:
        print('没有重复元素')


def findRepetition(arrays):
    initArrays = [-1] * (len(arrays) + 1)
    print(initArrays)
    for item in range(len(arrays)):
        if (-1 != initArrays[arrays[item]]):
            print("重复元素", arrays[item])
            break
        else:
            initArrays[arrays[item]] = arrays[item]
    else:
        print('没有重复元素')


if __name__ == '__main__':
    test()
