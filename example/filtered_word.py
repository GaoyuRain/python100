import os
from random import randint


def get_filtered_words():
    file = open('filtered_words', 'r')
    filter_list = []
    while True:
        text = file.readline()
        if not text:
            break
        # print(text01)
        filter_list.append(text.replace('\n', ''))
    file.close()
    return filter_list


def text1():
    filt_words = get_filtered_words()
    words = input('请输入文本：')
    is_filt = False
    for w in filt_words:
        if words.find(w) != -1:
            is_filt = True
            break
    print('freedom' if is_filt else 'Human Rights')


def text2():
    words = input('请输入文本：')
    filt_words = get_filtered_words()
    for w in filt_words:
        if words.find(w) != -1:
            words = words.replace(w, "**")
    print(words)


def text3():
    with open('filtered_words', 'r') as file:
        print(file.read())
    with open('filtered_words', 'r') as file1:
        for line in file1:
            print(line, end='__')
    with open('filtered_words', 'r') as file2:
        lines = file2.readlines()
    print(lines)


if __name__ == '__main__':
    print(get_filtered_words())
    # text3()
