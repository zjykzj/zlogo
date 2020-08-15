# -*- coding: utf-8 -*-

"""
@date: 2020/8/12 下午10:02
@file: cli.py.py
@author: zj
@description: 
"""

import os
import sys

from zlogo.config.defaults import default_argument_parser
from zlogo.util.misc import get_version, check_file_exist, check_dir_exist, generate_png, generate_svg_path
from zlogo.util.utility import parse_default_config, write_yaml_config


def parse():
    info = parse_default_config()
    # print(info)

    parser = default_argument_parser()
    args = parser.parse_args()
    # print(args)

    if args.version:
        print('pnno: v{}'.format(get_version()))
        sys.exit(0)

    if args.config_file:
        check_file_exist(args.font)
        config_info = parse_default_config(args.config_file)
        info.update(config_info)

    if args.logo:
        info['logo'] = args.logo
    if args.font:
        check_file_exist(args.font)
        info['font'] = args.font
    if args.fontsize:
        info['fontSize'] = args.fontsize
    if args.padding:
        info['padding'] = args.padding
    if args.color:
        info['path']['fill'] = args.color
    if args.output:
        check_dir_exist(args.output)
        info['output'] = generate_svg_path(args.output, info['logo'])
    # print(info)

    # 写入配置好的文件
    write_yaml_config(info)

    return info


def main():
    info = parse()

    # 执行logo生成操作
    flag = os.system('../tool/logo -c ../config/')
    if flag != 0:
        exit(0)

    # 同时生成.png图片
    generate_png(info['output'])


if __name__ == '__main__':
    main()
