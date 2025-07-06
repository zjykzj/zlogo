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


def _base_generate_png(svg_path, output_path, background_color=None):
    """
    使用 cairosvg 将 SVG 转换为 PNG 格式，并可选添加背景颜色。

    参数:
    svg_path -- SVG 文件的路径
    output_path -- 输出 PNG 文件的路径
    background_color -- 可选背景颜色（例如 '#ffffff' 表示白色）
    """
    if not check_file_exist(svg_path):
        print(f"\033[31mError: The file {svg_path} does not exist.\033[0m")
        return

    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()

        # 如果指定了背景颜色，则插入一个矩形作为背景
        if background_color:
            # 查找 <svg> 标签闭合位置
            svg_start_tag_end = svg_content.find('>')
            if svg_start_tag_end == -1:
                raise ValueError("Invalid SVG content")

            # 插入一个覆盖全图的矩形
            rect = f'<rect width="100%" height="100%" fill="{background_color}" />'
            svg_content = svg_content[:svg_start_tag_end + 1] + rect + svg_content[svg_start_tag_end + 1:]

        # 写入临时内存内容并转换
        cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), write_to=output_path)
        print(f"\033[32mGenerated: {output_path}\033[0m")
    except Exception as e:
        print(f"\033[31mError during conversion: {e}\033[0m")


def generate_png_with_transparency(svg_path, suffix="_transparent"):
    """
    生成带有透明背景的 PNG 图像
    """
    data_dir, svg_name = os.path.split(svg_path)
    img_name = os.path.splitext(svg_name)[0]
    png_path = os.path.join(data_dir, f"{img_name}{suffix}.png")
    _base_generate_png(svg_path, png_path)


def generate_png_with_white_background(svg_path, suffix="_white"):
    """
    生成带有白色背景的 PNG 图像
    """
    data_dir, svg_name = os.path.split(svg_path)
    img_name = os.path.splitext(svg_name)[0]
    png_path = os.path.join(data_dir, f"{img_name}{suffix}.png")
    _base_generate_png(svg_path, png_path, background_color="#ffffff")


# 示例调用
if __name__ == '__main__':
    svg_path = generate_svg_path(os.getcwd(), "example_logo")
    generate_png_with_transparency(svg_path)
    generate_png_with_white_background(svg_path)
