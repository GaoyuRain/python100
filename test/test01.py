"""
author :Rain
Date : 2019/08/03
Description :
"""


def test01():
    a = 'a'
    b = 'a'
    outid(a)
    outid(b)

    outspilt()

    c = 'hello'
    d = 'hello'
    outid(c)
    outid(d)
    print(c is d)

    outspilt()

    e = 'hello python'
    f = 'hello python'
    outid(e)
    outid(f)
    print(e is f)

    outspilt()

    g = 'hello ' + 'Python'
    h = 'hello ' + 'Python'
    outid(g)
    outid(h)
    print(g is h)


def test02():
    a1 = (1, 2, 3, 4)
    b1 = (1, 2, 3, 4)
    a2 = [1, 2, 3]
    a2.append(4)
    b2 = [1, 2, 3]
    outid(a1)
    outid(b1)
    print(a1 is b1)
    print('a1 hash:', hash(a1))
    print('b1 hash:', hash(b1))

    outspilt()

    d = 'a'
    outid(d)
    d += d
    outid(d)
    e = [1, 2]
    outid(e)
    e += e
    outid(e)


def outspilt():
    print('-' * 50)


def outid(data):
    print(str(data) + ':', id(data))


if __name__ == '__main__':
    test02()
