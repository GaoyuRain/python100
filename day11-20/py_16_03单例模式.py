"""
author :rain
Date : 2021/03/09
Description : 单例模式
"""
from functools import wraps
from threading import RLock


def singleton1(cls):
    """装饰类的装饰器-非线程安全"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        print(instances.__str__())
        return instances[cls]

    return wrapper


def singleton2(cls):
    """装饰类的装饰器-线程安全"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        print(instances.__str__())
        return instances[cls]

    return wrapper


@singleton1
class President1:
    pass


@singleton2
class President2:
    pass


if __name__ == '__main__':
    pre1_1 = President1()
    pre1_2 = President1()
    pre1_3 = President1()
    pre2_1 = President2()
    pre2_2 = President2()
    pre2_3 = President2()
    print(pre1_1, pre1_2, pre1_3, pre2_1, pre2_2, pre2_3)
