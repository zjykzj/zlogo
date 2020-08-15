# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:34
@file: misc.py
@author: zj
@description: 
"""

import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

import zlogo


def get_version():
    return zlogo.__version__


def check_file_exist(file_path):
    return os.path.isfile(file_path)


def generate_svg_path(dir_path, name):
    return os.path.join(dir_path, name + '.svg')


def generate_png(svg_path):
    data_dir, svg_name = os.path.split(svg_path)
    img_name = os.path.splitext(svg_name)[0]

    drawing = svg2rlg(svg_path)
    png_path = os.path.join(data_dir, img_name + '.png')
    renderPM.drawToFile(drawing, png_path, fmt="PNG")

    print(f'\033[32mGenerated: {png_path}\033[0m')
