# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:34
@file: utility.py
@author: zj
@description: 
"""

import os
import yaml


def get_file_dir():
    file_path = os.path.realpath(__file__)
    file_dir = os.path.split(file_path)[0]

    return file_dir


def parse_config(config_file=None):
    if not config_file:
        config_file = os.path.join(get_file_dir(), '../config/zlogo.logorc')
    # print(config_file)
    if not os.path.exists(config_file):
        raise ValueError('config_file must be specified')
    with open(config_file, 'r', encoding='utf-8') as f:
        info = yaml.load(f.read(), Loader=yaml.Loader)
        return info


def write_yaml_config(info: dict):
    assert isinstance(info, dict)

    yaml_config = os.path.join(get_file_dir(), '../config/.logorc')
    with open(yaml_config, "w", encoding="utf-8") as f:
        yaml.dump(info, f)
