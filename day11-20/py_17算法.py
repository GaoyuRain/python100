"""
author :rain
Date : 2020/10/12
Description :
"""
import math
import random


def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    print(items)
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                # items[j], items[i] = items[i], items[j]
                print(items)
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print(items)
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


# 完美数  对于一个 正整数，它和除了它自身以外的所有 正因子 之和相等
def checkPerfectNumber(num: int) -> bool:
    if num < 1 or num > math.pow(10, 8):
        return False
    d = 0
    for i in range(num - 1):
        n = i + 1
        if num % n == 0:
            print(n)
            d += n
    print(d)
    return True if d == num else False


if __name__ == '__main__':
    # data = [14, 2, 0, 5, 1, 2, 6, 8, 3, 5, 11, 13, 4, 9]
    # print(select_sort(data))
    # print(bubble_sort(data))
    # print(checkPerfectNumber(501))

    for i in range(501):
        if 501%(i+1)==0:
            print(i+1)

