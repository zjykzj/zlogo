# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:34
@file: misc.py
@author: zj
@description: 
"""

import os
import cairosvg

from zlogo import __version__ as zlogo_version


def get_version():
    """获取zlogo工具的版本号"""
    return zlogo_version


def check_file_exist(file_path):
    """检查指定文件路径是否存在"""
    return os.path.isfile(file_path)


def generate_svg_path(dir_path, name):
    """生成SVG文件的完整路径"""
    return os.path.join(dir_path, f"{name}.svg")


def generate_png(svg_path):
    """
    使用cairosvg将SVG文件转换为PNG格式。

    参数:
    svg_path -- SVG文件的路径
    """
    if not check_file_exist(svg_path):
        print(f"\033[31mError: The file {svg_path} does not exist.\033[0m")
        return

    data_dir, svg_name = os.path.split(svg_path)
    img_name = os.path.splitext(svg_name)[0]
    png_path = os.path.join(data_dir, f"{img_name}.png")

    try:
        # 使用cairosvg进行转换
        with open(svg_path, 'rb') as svg_file:
            cairosvg.svg2png(bytestring=svg_file.read(), write_to=png_path)
        print(f"\033[32mGenerated: {png_path}\033[0m")
    except Exception as e:
        print(f"\033[31mError during conversion: {e}\033[0m")


# 示例调用
if __name__ == '__main__':
    svg_path = generate_svg_path(os.getcwd(), "example_logo")
    generate_png(svg_path)
