"""
author :xlf
Date : 2022/12/13
Description : 单例
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


class SinglePage():
    # 常见单例
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        '''为对象分配空间并返回对象的引用'''
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第⼀个对象分配空间
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, data):
        if not SinglePage.init_flag:
            # 举例传递参数，可以不用
            super().__init__(data)
            SinglePage.init_flag = True


@singleton1
class President1:
    pass


@singleton2
class President2:
    pass


class President3:
    pass


if __name__ == '__main__':
    pre1_1 = President1()
    pre1_2 = President1()
    pre1_3 = President1()
    pre2_1 = President2()
    pre2_2 = President2()
    pre2_3 = President2()
    print(pre1_1, pre1_2, pre1_3, pre2_1, pre2_2, pre2_3)
