"""
author :xlf
Date : 2022/12/13
Description :
"""


def get_distance_count(high: float = 300, bounce=0.25, distance: float = 0, num=0):
    """
    high:start distance
    bounce：bounce ratio
    distance:total running distance
    num: total bounce num
    """
    num = num + 1
    last_high = high * bounce
    distance = distance + high + last_high
    if last_high <= 0.0001:
        return num, distance, last_high
    return get_distance_count(high=last_high, distance=distance, num=num)


if __name__ == '__main__':
    print(get_distance_count())
