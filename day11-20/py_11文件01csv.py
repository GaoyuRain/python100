"""
author :rain
Date : 2021/01/20
Description :
"""

import csv
import random


def test001():
    # Python标准库中的csv模块，该模块的writer函数会返回一个csvwriter对象，
    # 通过该对象的writerow或writerows方法就可以将数据写入到CSV文件中
    with open('../filedir/scores.csv', 'w') as file:
        # writer = csv.writer(file)
        writer = csv.writer(file, delimiter="|", quoting=csv.QUOTE_ALL)
        writer.writerow(['姓名', '语文', '数学', '英语'])
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        for i in range(5):
            verbal = random.randint(50, 100)
            math = random.randint(40, 100)
            english = random.randint(30, 100)
            writer.writerow([names[i], verbal, math, english])


def test002():
    # 读
    with open('../filedir/scores.csv', 'r+') as file:
        reader = csv.reader(file, delimiter='|')
        # reader = csv.reader(file)
        # print(reader.line_num)
        for line in reader:
            print(reader.line_num, end='\t')
            for elem in line:
                print(elem, end='\t')
            print()


def test003():
    # 去除csv文件中的空行
    with open('../filedir/baoxiao.csv', 'r+') as file:
        for row in csv.reader(file):
            for elem in row:
                if elem is not None:
                    print(row)
                    with open('../filedir/baoxiao1.csv', 'a+') as f:
                        writer = csv.writer(f)
                        writer.writerow(row)


if __name__ == '__main__':
    # test001()
    test003()
