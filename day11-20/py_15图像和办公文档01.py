"""
author :rain
Date : 2020/09/04
Description :
"""

from PIL import Image


def test1():
    image = Image.open('../filedir/test1.png')
    rect = 80, 20, 310, 360
    size = 128, 128
    # 裁剪
    # image.crop(rect).show()
    # 压缩
    # image.thumbnail(size)
    # image.show()
    # 旋转
    # image.rotate(180).show()
    # 翻转
    image.transpose(Image.FLIP_LEFT_RIGHT).show()


def main():
    pass


if __name__ == '__main__':
    test1()
