"""
author :rain
Date : 2020/10/12
Description :
"""


def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    print(items)
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    data = [2, 5, 1, 2, 6, 8, 3, 5, 9]
    print(select_sort(data))
