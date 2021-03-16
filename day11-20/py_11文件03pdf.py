"""
author :rain
Date : 2021/02/05
Description :
"""

import random

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

def test02():
    # 创建Canvas对象（PDF文档对象）
    doc = canvas.Canvas('../filedir/demo.pdf', pagesize=A4)
    # 获取A4纸的尺寸
    width, height = A4
    # 读取图像
    image = canvas.ImageReader('../filedir/jiduo.png')
    # 通过PDF文档对象的drawImage绘制图像内容
    doc.drawImage(image, (width - 250) // 2, height - 475, 250, 375)
    # 设置字体和颜色
    doc.setFont('Helvetica', 32)
    doc.setFillColorRGB(0.8, 0.4, 0.2)
    # 通过PDF文档对象的drawString输出字符串内容
    doc.drawString(10, height - 50, "Life is short, I use Python!")
    # 保存当前页创建新页面
    doc.showPage()
    # 准备表格需要的数据
    scores = [[random.randint(60, 100) for _ in range(3)] for _ in range(5)]
    names = ('Alice', 'Bob', 'Jack', 'Lily', 'Tom')
    for row, name in enumerate(names):
        scores[row].insert(0, name)
    scores.insert(0, ['Name', 'Verbal', 'Math', 'Logic'])
    # 创建一个Table对象（第一个参数是数据，第二个和第三个参数是列宽和行高）
    table = Table(scores, 50, 20)
    # 设置表格样式（对齐方式和内外边框粗细颜色）
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.red),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
    ]))
    table.split(0, 0)
    # 通过Table对象的drawOn在PDF文档上绘制表格
    table.drawOn(doc, (width - 200) // 2, height - 150)
    # 保存当前页创建新页面
    doc.showPage()
    # 保存PDF文档
    doc.save()

if __name__ == '__main__':
    test02()