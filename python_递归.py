import os
import sys


def all_dir(file_path):
    # os.chdir(file_path)
    # print('-' * 50)
    # print(file_path)
    list_dir = os.listdir(file_path)
    # print('file_path:', list_dir)
    for file_name in list_dir:
        print(file_name)
        if os.path.isdir(file_path + '\\' + file_name):
            all_dir(file_path + '\\' + file_name)
        # else:
        #     print(file_name)


if __name__ == '__main__':
    # all_dir()
    # print(os.getcwd())
    all_dir(os.getcwd())
