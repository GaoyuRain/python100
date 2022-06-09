"""
author :rain
Date : 2021/04/29
Description :
"""
import copy
import heapq
from collections import Counter
from collections.abc import Iterable


def test01():
    # 给出一个数组列表，输出一个字典 key为去除重复后的数字,按大小排序，value为出现的次数
    # 解法1：
    data = [1, 2, 2, 4, 4, 2, 6, 3, 7, 9, 5, 2, 4, 9]
    results = {}
    for i in range(data.__len__()):
        key = data[i]
        values = 0
        for l in range(data.__len__()):
            if key == data[l]:
                values += 1
        results.update({key: values})
    results = sorted(results.items(), reverse=True)
    # results = sorted(results.items(), key=lambda x: x[0], reverse=True)
    print(dict(results))

    #  解法2：使用Counter 计数器
    a = 'apple'  # 也可以统计字符串每个单词出现的次数
    # a = [1, 2, 2, 4, 4, 2, 6, 3, 7, 9, 5, 2, 4, 9]
    res = Counter(a)
    res.update('apple')
    res = dict(res)
    print(res)
    # 按健大小排序
    res = sorted(res.items(), key=lambda x: x[0], reverse=True)
    print(dict(res))


def test02():
    #  lambda函数实现两个数相乘
    sum01 = lambda a, b: a * b
    print(sum01(2, 3))


def test03():
    # 字典根据健从大到小排序
    data = {"name": "rain", "age": 18, "city": "china"}
    print(data.items())
    data = sorted(data.items(), key=lambda x: x[0], reverse=False)
    print(dict(data))


def test04():
    # 列出列表所有奇数并构造新列表
    a = [1, 2, 2, 4, 4, 2, 6, 3, 7, 9, 5, 2, 4, 9]

    # 方法1：
    def fn(a):
        return a % 2 == 1

    # 接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
    # 然后返回 True 或 False，最后将返回 True 的元素放到新列表  # filter 返回一个iterator
    newlist1 = list(filter(fn, a))
    # 方法2：
    newlist2 = [i for i in a if i % 2 == 1]

    print(newlist2)


def test05():
    # 两个有序列表合并成一个有序列表
    a = [1, 3, 5]
    b = [1, 1, 2, 4, 6]
    # c = [b.append(i) for i in a]
    # 方法1：复杂版
    c = []
    while a and b:
        if a[0] < b[0]:
            c.append(a[0])
            del a[0]
        else:
            c.append(b[0])
            del b[0]
    if a:
        c.extend(a)
    if b:
        c.extend(b)
    print(c)
    # 方法 2
    a.extend(b)
    a.sort()


def test06():
    # 列出字典中值 为 95 的 key
    data = {'a': 90, 'b': 95, 'c': 85, 'd': 95}
    name = [i for i in data.keys() if data.get(i) == 95]
    print(name)
    # 列表展开


def test07():
    # a = (1, 2)
    a = [1, 2]
    b = copy.deepcopy(a)
    b1 = copy.copy(a)
    print('a:' + str(id(a)))
    print('b:' + str(id(b)))
    print('b:' + str(id(b1)))


def qp01():
    a = 'abcde'
    a.strip()
    print(a[-4:-1:2])


def isIterable():
    # 是否是可迭代对象
    print(isinstance('abc', Iterable))


def indexList():
    for i, value in enumerate(['a', 'b', 'c', 'd']):
        print(i, value)


def creatList():
    print('-' * 100)
    print('creatList')
    list1 = [x + y for x in '123' for y in 'abc']
    print(list1)
    list2 = [x if x % 2 == 0 else -x for x in range(1, 11)]
    print(list2)
    L = ['Hello', 'World', 18, 'Apple', None]
    l1 = [s.lower() for s in L if isinstance(s, str)]
    print(l1)


def testFunc():
    print(abs)
    print(type(abs(-199)))



if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # isIterable()
    # indexList()
    # creatList()
    testFunc()
