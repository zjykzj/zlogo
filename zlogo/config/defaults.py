# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:15
@file: defaults.py
@author: zj
@description: 
"""

import argparse


def default_argument_parser():
    """
    Create a parser with some common arguments used by users.

    Returns:
        argparse.ArgumentParser:
    """
    parser = argparse.ArgumentParser(description='custom logo - ZLOGO')

    ### Positional arguments

    ### Optional arguments

    parser.add_argument('-l', '--logo', metavar='LOGO', type=str, help='specify the logo text')
    parser.add_argument('-f', '--font', metavar='FONT', type=str, help='path to a font file(.ttf)')
    parser.add_argument('-fs', '--fontsize', metavar='FontSize', type=int, help="specify the font size")
    parser.add_argument('-p', '--padding', metavar='PADDING', type=int, help='specify the border size')
    parser.add_argument('--color', metavar='COLOR', type=str, help="sepcify the text' color")

    parser.add_argument('-c', "--config_file", metavar="CONFIG_FILE", type=str, help="path to config file")

    parser.add_argument('-o', "--output", metavar='OUTPUT', type=str, help="path to output file(.svg)")

    parser.add_argument('-v', '--version', help='output version infomation', action="store_true"),

    return parser


if __name__ == '__main__':
    parser = default_argument_parser()
    print(parser.parse_args())
    print(parser)
