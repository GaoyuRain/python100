"""
author :rain
Date : 2020/09/04
Description :
"""
import heapq
import itertools


def test01():
    # 嵌套列表
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
            print(scores)


def test02():
    # 生成式
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    prices1 = {name: price for name, price in prices.items() if price > 100}
    print(prices1)


def test03():
    # 堆排序
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    # 最大的三个
    print(heapq.nlargest(3, list1))
    # 最小的三个
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


def test04():
    # 迭代器
    data = 'abcd'
    # 产生ABCD的全排列
    d1 = itertools.permutations(data)
    # 产生无限循环序列
    # d1 = itertools.cycle(data)
    # 产生ABCDE的所有五选三组合
    d1 = itertools.combinations('ABCDE', 3)
    # 产生ABCD和123的笛卡尔积
    d1 = itertools.product('ABCD', '123')
    for i in d1:
        print(i)

    c = itertools.accumulate(data)
    for i in c:
        print(i)


    # 累加值进行迭代，字典累加key的值
    d = {'a': 1, 'b': 2, 'c': 3}
    c = itertools.accumulate(d)
    for i in c:
        print(i)


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    test04()
