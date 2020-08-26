import os
import random
import time


def test01():
    '''
    练习1：在屏幕上显示跑马灯文字
    :return:
    '''
    content = '北京欢迎你，为你开天辟地。。。'
    print(content[1:])
    print(content[0])
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        # content = content[1:] + content[0]
        content = content[1:] + content[0]


def test02():
    '''转义符'''
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')


def test03():
    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    list1 = [1, 3, 5, 7, 100]
    # print(enumerate(list1).__str__())
    for index, elem in enumerate(list1):
        print(index, elem)


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lat_pos = len(all_chars) - 1
    cod = ''
    for _ in range(code_len):
        pos = random.randint(0, lat_pos)
        cod += all_chars[pos]
    return cod


def get_suffix(filename, hasdot=False):
    '''
    获取文件名的后缀名
    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if hasdot else pos + 1
        return filename[index:]
    else:
        return ''


def get_max(num_list: list):
    '''
    设计一个函数返回传入的列表中最大和第二大的元素的值。
    :return:
    max1 = sorted(num_list, reverse=True)[0]
    max2 = sorted(num_list, reverse=True)[1]
    return max1, max2
    '''
    max1, max2 = num_list[0], num_list[1] if num_list[0] > num_list[1] else (num_list[1], num_list[0])
    for index in range(2, len(num_list)):
        if num_list[index] > max1:
            max2 = max1
            max1 = num_list[index]
        elif num_list[index] > max2:
            max2 = num_list[index]
    return max1, max2


def yh_text():
    '''
    杨辉三角
    :return:
    '''
    num = int(input('Number of rows: '))
    yh = [[]] * num
    print(yh)
    print(type(yh))
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    # test01()
    # print(generate_code())
    # print(get_suffix('name.tar.gz', True))
    # print(get_max([2, 1, 6, 3, 9, 10, 2, 7, 29]))
    # print(get_max(['d', 'a', 'c', 'b', 'cd']))
    # yh_text()
    # test03()
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'bd', 'c'], '12345'))
    print(items2)
