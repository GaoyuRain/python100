"""
author :rain
Date : 2020/09/01
Description :可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化
"""

from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def play(self):
        pass


class Dog(Pet):
    def __init__(self, nickname):
        super().__init__(nickname)

    def play(self):
        print('play meat')


if __name__ == '__main__':
    dog = Dog('hei')
