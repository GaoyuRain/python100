from time import sleep
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 获取锁
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 释放锁
            self._lock.release()

    # def deposit(self, money):
    #     new_balance = self._balance + money
    #     sleep(0.01)
    #     self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account: Account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    threads = []
    account = Account()
    for i in range(200):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    print(account.balance)


if __name__ == '__main__':
    main()
