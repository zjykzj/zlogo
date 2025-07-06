# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:15
@file: defaults.py
@author: zj
@description: 
"""

import argparse
from typing import Optional


def default_argument_parser() -> argparse.ArgumentParser:
    """
    创建一个通用的命令行参数解析器，用于 ZLOGO 工具。

    支持以下功能：
    - 指定 LOGO 文字内容、字体、字号、颜色、边距等；
    - 通过配置文件加载默认值；
    - 指定输出路径；
    - 查看版本信息。

    Returns:
        argparse.ArgumentParser: 配置好的命令行解析器对象
    """
    # parser = argparse.ArgumentParser(description="Custom Logo Generator - ZLOGO")
    #
    # # Input Configuration Group
    # input_group = parser.add_argument_group("Input Configuration")
    # input_group.add_argument('-l', '--logo', metavar='LOGO', type=str,
    #                          help='指定生成的 LOGO 文字内容（例如：ZLOGO）')
    # input_group.add_argument('-f', '--font', metavar='FONT', type=str,
    #                          help='指定字体文件路径（.ttf 格式）')
    # input_group.add_argument('-fs', '--fontsize', metavar='FontSize', type=int,
    #                          help='指定字体大小（例如：64）')
    # input_group.add_argument('--color', metavar='COLOR', type=str,
    #                          help='指定文字颜色（十六进制或英文名称，例如：#2b68a7）')
    #
    # # Layout and Padding Group
    # layout_group = parser.add_argument_group("Layout and Padding")
    # layout_group.add_argument('-p', '--padding', metavar='PADDING', type=int,
    #                           help='指定统一的边距（覆盖上下左右）')
    #
    # # File I/O Group
    # file_group = parser.add_argument_group("File I/O")
    # file_group.add_argument('-c', '--config_file', metavar='CONFIG_FILE', type=str,
    #                         help='指定配置文件路径（YAML 格式）')
    # file_group.add_argument('-o', '--output', metavar='OUTPUT', type=str,
    #                         help='指定输出 SVG 文件路径（例如：./logo.svg）')
    #
    # # Misc Group
    # misc_group = parser.add_argument_group("Miscellaneous")
    # misc_group.add_argument('-v', '--version', action='store_true',
    #                         help='显示版本信息并退出')
    #
    # return parser
    parser = argparse.ArgumentParser(description="Custom Logo Generator - ZLOGO")

    # Input Configuration Group
    input_group = parser.add_argument_group("Input Configuration")
    input_group.add_argument('-l', '--logo', metavar='LOGO', type=str,
                             help='Specify the logo text (e.g., ZLOGO)')
    input_group.add_argument('-f', '--font', metavar='FONT', type=str,
                             help='Path to a TrueType font file (.ttf)')
    input_group.add_argument('-fs', '--fontsize', metavar='FontSize', type=int,
                             help='Set the font size (e.g., 64)')
    input_group.add_argument('--color', metavar='COLOR', type=str,
                             help='Set the text color (hex or name, e.g., #2b68a7)')

    # Layout and Padding Group
    layout_group = parser.add_argument_group("Layout and Padding")
    layout_group.add_argument('-p', '--padding', metavar='PADDING', type=int,
                              help='Set uniform padding around the text (overrides individual padding values if set)')

    # File I/O Group
    file_group = parser.add_argument_group("File I/O")
    file_group.add_argument('-c', '--config_file', metavar='CONFIG_FILE', type=str,
                            help='Path to a YAML configuration file')
    file_group.add_argument('-o', '--output', metavar='OUTPUT', type=str,
                            help='Output SVG file path (e.g., ./logo.svg)')

    # Miscellaneous Group
    misc_group = parser.add_argument_group("Miscellaneous")
    misc_group.add_argument('-v', '--version', action='store_true',
                            help='Show version information and exit')

    return parser


if __name__ == '__main__':
    parser = default_argument_parser()
    args = parser.parse_args()
    print(f"Parsed arguments: {args}")
