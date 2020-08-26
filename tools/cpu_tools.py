"""
author :Rain
Date : 2019/03/25
Description :实时获取android应用内存使用和cpu占用信息
"""
import os
import re
import subprocess
from time import sleep

from matplotlib import pyplot as plt
from matplotlib import animation
import psutil


def getTotalMemo(packagename):
    '''获取占用内存信息'''
    lines: list[str] = os.popen('adb shell dumpsys meminfo ' + packagename).readlines()
    for line in lines:
        if re.findall('TOTAL', line):  # 找到TOTAL 这一行
            data = line.split(' ')
            while '' in data:
                data.remove('')
            return data[1]


def getCPUinfo(packagename):
    '''获取占用cpu信息'''
    # lines: list[str] = os.popen("adb shell top -m 200 -n 1 -s cpu").readlines()
    # adb shell  top - m 100 - n  1
    line: str = os.popen("adb shell top -m 200 -n 1  | findstr " + packagename[0:15:1]).readline()
    cpuList = line.split(' ')
    while '' in cpuList:
        cpuList.remove('')
    return float(cpuList[3].strip('%'))


fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1, xlim=(0, 100), ylim=(0, 350))
ax2 = fig.add_subplot(2, 1, 2, xlim=(0, 100), ylim=(0, 100))
line, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)
x = []
y = []
y2 = []


def init():
    line.set_data([], [])
    line.set_data([], [])
    return line, line2


def getx():
    t = "0"
    return t


def animate(i, packagename):
    x.append(int(getx()) + i)
    y.append(int(getTotalMemo(packagename)) / 1024)  # 每执行一次去获取一次值加入绘制的data中
    y2.append(getCPUinfo(packagename))
    print(x, y)
    line.set_data(x, y)
    line2.set_data(x, y2)
    return line, line2


def top_cpu(packagename):
    cpu = 0
    cmd = "adb shell dumpsys cpuinfo | grep " + packagename
    # cmd = "adb shell top -n %s -s cpu | grep %s$" %(str(times), pkg_name)
    top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for info in top_info:
        cpu = info.split()[2].decode()  # bytes转换为string
    print("cpu占用:%s" % cpu)
    return cpu


if __name__ == '__main__':
    # print(getTotalMemo('com.kohler.mirror'))
    # print(getCPUinfo('com.kohler.mirror'))
    # animate(10,'com.duowan.kiwi')
    # while True:
    #     sleep(2)
    # anim1 = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=30)
    # plt.show()
    top_cpu('com.duowan.kiwi')

    # print(psutil.cpu_times())
