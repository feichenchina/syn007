#!/usr/bin/python3
#可用的预定义文件模板变量为：
# 当前项目的名称-->yiguo
#文件名---》verification
#用户名---》Administrator
#日期-----》2019/10/31 
#时间-----》7:57
#功能-----》
# !/usr/bin/python
# -*- coding: utf-8 -*-

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class VerificationCode:
    # 生成几位数的验证码
    number = 4
    # 生成验证码图片的宽高
    size = (102, 34)
    # 背景颜色，默认为白色
    bg_color = (255, 255, 255)
    # 字体颜色，默认为蓝色
    font_color = (0, 0, 255)
    # 干扰线颜色。默认为红色
    line_color = (255, 0, 0)
    # 干扰点颜色。默认为蓝色
    point_color = (0, 0, 255)
    # 加入干扰线条数
    line_number = 3
    # 干扰点的个数
    point_number = 30

    # 用来随机生成一个字符串
    def gene_text(self):
        letters = "23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"  # 元字符
        return ''.join(random.sample(list(letters), self.number))  # 生成位数为number的验证码

    # 用来绘制干扰线
    def gene_line(self, draw, width, height):
        for i in range(self.line_number):
            begin = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0, width), random.randint(0, height))
            draw.line([begin, end], fill=self.line_color)

    # 增加干扰点
    def gene_point(self, draw, width, height):
        point_list = []
        for i in range(self.point_number):
            point = (random.randint(0, width), random.randint(0, height))
            point_list.append(point)
        draw.point(point_list, fill=self.point_color)

    # 生成验证码
    def gene_code(self):
        width, height = self.size  # 图片宽高
        image = Image.new('RGBA', self.size, self.bg_color)  # 创建图片
        font = ImageFont.truetype('arial', 25)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = self.gene_text()  # 生成字符串
        font_width, font_height = font.getsize(text)  # 验证码占宽高
        draw.text(((width - font_width) / self.number + 5, (height - font_height) / self.number), text,
                  font=font, fill=self.font_color)  # 填充字符串
        self.gene_line(draw, width, height)  # 增加干扰线
        self.gene_point(draw, width, height)  # 增加干扰点
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
        # image.save('idencode.png')  # 保存验证码图片
        return text, image

# 调用一下试试
if __name__ == '__main__':

    text,image = VerificationCode().gene_code()
    print(text)
    image.show(image)