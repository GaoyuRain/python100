"""
author :rain
Date : 2021/01/20
Description :
"""

import os
import subprocess


def test01():
    # 导入os模块
    command_list = 'pip3 list'
    command_install = 'pip install '
    data = os.popen(command_list)
    # subprocess.call(command_list, shell=True)
    lines = data.readlines()  # 读取命令行的输出到一个list
    # 删除表头信息
    # del info[0]
    # del info[0]
    print(lines)
    # for line in lines:  #按行遍历
    #     # 用" "分割每行，列表的第一个就是包名
    #     package = line.split(" ")[0]
    #     print("正在检查更新" + package)
    #     os.system(command_upgrade+package+" --upgrade")


if __name__ == '__main__':
    test01()