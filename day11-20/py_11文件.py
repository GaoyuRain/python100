import os
from math import sqrt
import json


def is_prime(n):
    '''
    判断素数的函数
    :param n:
    :return:
    '''
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


# 1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）。
def save_prime():
    os.chdir('../filedir/')
    filenames = ['a.txt', 'b.txt', 'c.txt']
    fs_list = []
    try:
        for fliename in filenames:
            fs_list.append(open(fliename, 'a', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + ',')
                elif number < 1000:
                    fs_list[1].write(str(number) + ',')
                else:
                    fs_list[2].write(str(number) + ',')
    except IOError as er:
        print(er)
        print('写文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()


def copy_pic():
    '''
    复制图片
    :return:
    '''
    global file1, file2
    try:
        os.chdir('../filedir/')
        # with open('python.png', 'rb') as fil1:
        #     data = fil1.read()
        # with open('jiduo.png', 'wb') as fil2:
        #     fil2.write(data)
        file1 = open('python.png', 'rb')
        file2 = open('jiduo.png', 'wb')
        while True:
            data = file1.readline()
            print(data)
            if len(data) != 0:
                file2.write(data)
            else:
                break
    except FileNotFoundError as e:
        print('文件无法打开错误：', e)
    except IOError as e:
        print('io error:')
    finally:
        file1.close()
        file2.close()


def copy_big_pic():
    # 如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销，为了减少对内存的占用，
    # 可以为read方法传入size参数来指定每次读取的字节数，通过循环读取和写入的方式来完成上面的操作
    try:
        with open('python.png', 'rb') as file1, \
                open('python.png', 'wb') as file2:
            data = file1.read(512)
            while data:
                file2.write(data)
                data = file1.read()
    except FileNotFoundError:
        print('指定的文件无法打开.')
    except IOError:
        print('读写文件时出现错误.')
    print('程序执行结束.')


def save_json():
    '''
    json 文件处理
    :return:
    '''
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]}
    # contnet = json.dumps(mydict)
    # print(contnet)
    try:
        os.chdir('../filedir/')
        with open('data.json', 'w', encoding='utf-8') as cont:
            json.dump(mydict, cont)
    except IOError as e:
        print('io error：', e)


def get_json():
    try:
        os.chdir('../filedir/')
        with open('data.json', 'r', encoding='utf-8') as cont:
            # data = json.loads(cont.read())
            data = json.load(cont)
            print(data)
    except IOError as e:
        print('io error：', e)


def text1(num):
    num = num.upper()
    print(num)


if __name__ == '__main__':
    # save_prime()
    test = 'hello'
    # copy_pic()
    # save_json()
    get_json()
