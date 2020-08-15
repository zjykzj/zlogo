# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:34
@file: utility.py
@author: zj
@description: 
"""

import yaml


def parse_default_config(config_file='../config/zlogo.logorc'):
    if not config_file:
        raise ValueError('config_file must be specified')
    with open(config_file, 'r', encoding='utf-8') as f:
        info = yaml.load(f.read(), Loader=yaml.Loader)
        return info


def write_yaml_config(info: dict):
    assert isinstance(info, dict)

    with open("../config/.logorc", "w", encoding="utf-8") as f:
        yaml.dump(info, f)
