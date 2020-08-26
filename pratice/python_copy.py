import os
import time


def copy_movie():
    try:
        file1 = open('junhuofan.mkv', 'rb')
        file2 = open('junhuofan_copy.mkv', 'wb')
        while True:
            data = file1.readline()
            if len(data) == 0:
                break
            file2.write(data)
    except IOError as e:
        print('ioerror:', e)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    time1 = time.time()
    copy_movie()
    time2 = time.time()
    print('耗时：', time2 - time1)
