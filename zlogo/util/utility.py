# -*- coding: utf-8 -*-

"""
@date: 2020/8/14 下午10:34
@file: utility.py
@author: zj
@description: 
"""

import yaml

from pathlib import Path
from typing import Optional, Dict


def get_file_dir() -> str:
    """
    获取当前模块文件所在的绝对路径目录。

    Returns:
        str: 当前文件所在目录的绝对路径
    """
    file_path = Path(__file__).resolve()
    return str(file_path.parent)


def parse_config(config_file: Optional[str] = None) -> Dict:
    """
    解析YAML配置文件并返回其内容字典。

    Args:
        config_file (str, optional): 配置文件路径。如果未提供，则使用默认路径 '../config/zlogo.logorc'。

    Returns:
        dict: 解析后的配置信息

    Raises:
        ValueError: 如果指定的配置文件不存在
        yaml.YAMLError: 如果配置文件格式不正确
    """
    if not config_file:
        default_config_path = Path(get_file_dir()) / '..' / 'config' / 'zlogo.logorc'
        config_file = str(default_config_path.resolve())

    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_file}")

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            info = yaml.load(f.read(), Loader=yaml.Loader)
            return info or {}
    except yaml.YAMLError as e:
        raise ValueError(f"YAML 格式错误: {e}") from e


def write_yaml_config(info: Dict) -> None:
    """
    将配置信息写入临时YAML文件 '.logorc'。

    Args:
        info (dict): 要写入的配置字典

    Raises:
        AssertionError: 如果输入不是字典类型
    """
    assert isinstance(info, dict), "参数 'info' 必须是一个字典"

    config_path = Path(get_file_dir()) / '..' / 'config' / '.logorc'
    config_path.parent.mkdir(parents=True, exist_ok=True)  # 确保目录存在

    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(info, f, allow_unicode=True)
    except Exception as e:
        raise RuntimeError(f"写入配置文件失败: {e}") from e


if __name__ == '__main__':
    # 测试解析配置
    config = parse_config()
    print("Loaded config:", config)

    # 测试写入配置
    test_info = {
        "logo": "test_logo",
        "color": "#FF0000"
    }
    write_yaml_config(test_info)
    print("Test config written to .logorc")
