"""
author :rain
Date : 2020/09/01
Description :
"""


class Company:
    __slots__ = ('_boss', '_normal', '_default')

    def __init__(self, boss, normal):
        self._boss = boss
        self._normal = normal

    @staticmethod
    def is_boss(name: str):
        return True if name[0].upper() == 'X' else False

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        self._boss = boss

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, normal):
        self._normal = normal


if __name__ == '__main__':
    company = Company('laow', 'Xiaow')
    company.normal = 'XL'
    company._default = 'XX'
    # company._other = 'hh'
    print(company.normal)
    print(company.is_boss('xx'))
