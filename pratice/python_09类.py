from abc import ABCMeta, abstractmethod

"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""


class Employee:
    __count = 1

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_slalry(self):
        pass

    @classmethod
    def get_count(cls):
        return cls.__count


class Manger(Employee):

    def get_slalry(self):
        return 15000


class Programmer(Employee):

    # def __new__(cls, *args, **kwargs):
    #     print(id(cls))

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_slalry(self):
        # super().text()
        return self._working_hour * 150

    def __str__(self):
        # print('name:', self.name, '，工资：', self.get_slalry(), ',hehe')
        return 'name:' + self.name + '，工资：' + str(self.get_slalry()) + ',hehe'


class Slaesman(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_slalry(self):
        return 1200 + self._sales * 0.05

    # def get_slalry(self, name):
    #     return 1200 + self._sales * 0.05 + 200


def main():
    emps = [
        Manger('刘备'), Programmer('诸葛亮'),
        Manger('曹操'), Slaesman('荀彧'),
        Slaesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]

    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入 %s 工作时长:' % emp.name))
        elif isinstance(emp, Slaesman):
            emp.sales = int(input("请输入 %s 销售额:" % emp.name))
        print('%s 的工资为:%s' % (emp.name, emp.get_slalry()))


if __name__ == '__main__':
    # main()
    # libei = Programmer('刘备')
    # # print(dir(libei))22
    # print(libei)
    # liubei = Programmer('刘备')
    # zhangfei = Programmer('张飞')
    # print(liubei.name)
    # print('id(liubei.name):', id(liubei.name))
    # print('id(liubei.get_slalry):', id(liubei.get_slalry))
    # print('id(liubei):', id(liubei))
    # print('*' * 10)
    # print('id(zhangfei.name):', id(zhangfei.name))
    # print('id(zhangfei.get_slalry):', id(zhangfei.get_slalry))
    # print('id(zhangfei):', id(zhangfei))
    # print('id(Programmer):', id(Programmer))
    # print(Manger.get_count())
    def text(num):
        print('num1:', id(num))
        # num += [30]
        num = num + [30]
        print('num2:', id(num))
        num = [1, 2]
        print('num3:', id(num))


    num = [10, 20]
    print('num0:', id(num))
    text(num)
