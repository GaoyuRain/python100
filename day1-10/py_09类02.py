"""
author :rain
Date : 2020/09/01
Description :
"""
from time import localtime, time, sleep


class Clock:

    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        # print(ctime.__str__())
        return cls(ctime.tm_year, ctime.tm_mon, ctime.tm_mday, ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
        sleep(1)

    def time(self):
        """显示时间"""
        return '%02d年%02d月%02d日 %02d:%02d:%02d' % (self.year, self.month, self.day, self.hour, self.minute, self.second)


class BeautyClock(Clock):
    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, second=0, title=''):
        super().__init__(year, month, day, hour, minute, second)
        self._title = title
        print(self._title)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def time(self):
        """显示时间"""
        return self._title + '%02d年%02d月%02d日 %02d:%02d:%02d' % (
            self.year, self.month, self.day, self.hour, self.minute, self.second)


if __name__ == '__main__':
    # clock = Clock.now()
    # clock.time()
    # while True:
    #     print(clock.time())
    #     clock.run()
    # 类方法也能继承
    byClock = BeautyClock(title='Now Time:').now()
    print(byClock.time())
    byClock.title = 'Now Time:'
    print(byClock.time())
