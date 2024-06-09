# 参考资料
# [Python3 用PIL处理图像（二）——将图片装换成素描](https://blog.csdn.net/u014663232/article/details/105777826)

import argparse
import os
import sys
from PIL import Image, ImageFilter, ImageOps

mode_dict = {1: '黑白', 2: '素描', 3: '浮雕', 4: '模糊', 5: '锐化'}


def parse_args():
    parser = argparse.ArgumentParser(description=f'程序功能：图像处理（{"，".join([v for v in mode_dict.values()])}）')
    parser.add_argument('-i', '--input', required=True, type=str, help='输入图像')
    parser.add_argument('-o', '--output',
                        default='-1',
                        required=False, type=str, help='输出图像')
    parser.add_argument('-m', '--mode', default=2, type=int,
                        choices=[i for i in mode_dict.keys()],
                        help='图像处理模式: {}【默认为素描模式】'.format(mode_dict))
    parser.add_argument('-s', '--sketch', default=-1, type=int,
                        help='素描阴影程度【默认为-1，即不使用该参数而采用另一种算法】')
    parser.add_argument('-b', '--blur', default=0, type=int, help='模糊模式层数')
    parser.add_argument('-e', '--enhance', default=0, type=int, help='锐化模式层数')

    return parser.parse_args()


def imgProcessing():
    args = parse_args()
    img = Image.open(args.input)

    if args.mode == 1:
        img = img.convert('L')

    elif args.mode == 2:
        img = img.convert('L')
        img2 = img.copy()
        img2 = ImageOps.invert(img2)
        if args.sketch == -1:
            img = img.filter(ImageFilter.CONTOUR)
        else:
            for i in range(args.sketch):
                img2 = img2.filter(ImageFilter.BLUR)
            width, height = img.size
            for x in range(width):
                for y in range(height):
                    a = img.getpixel((x, y))
                    b = img2.getpixel((x, y))
                    img.putpixel((x, y), min(int(a * 255 / (256 - b)), 255))

    elif args.mode == 3:
        img = img.filter(ImageFilter.EMBOSS)

    for i in range(args.blur):
        img = img.filter(ImageFilter.BLUR)

    for i in range(args.enhance):
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    if args.output == '-1':
        file_name, file_ext = os.path.splitext(os.path.basename(args.input))
        args.output = file_name + "(" + mode_dict[args.mode] + ")" + file_ext

    img.save(args.output)


if __name__ == '__main__':
    imgProcessing()
