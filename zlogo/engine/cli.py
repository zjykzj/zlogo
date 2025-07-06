# -*- coding: utf-8 -*-

"""
@date: 2020/8/12 下午10:02
@file: cli.py.py
@author: zj
@description: 
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any

from zlogo.config.defaults import default_argument_parser
from zlogo.util.misc import get_version, check_file_exist, generate_png_with_white_background, generate_svg_path
from zlogo.util.utility import parse_config, write_yaml_config, get_file_dir


def parse_args_and_update_config() -> Dict[str, Any]:
    """
    Parse command-line arguments and update config accordingly.

    Returns:
        dict: Updated configuration dictionary.
    """
    # Load base config
    config = parse_config()

    # Parse command-line args
    parser = default_argument_parser()
    args = parser.parse_args()

    if args.version:
        print(f"zlogo: v{get_version()}")
        sys.exit(0)

    # Update with config file if provided
    if args.config_file:
        if not check_file_exist(args.config_file):
            raise FileNotFoundError(f"Config file not found: {args.config_file}")
        custom_config = parse_config(args.config_file)
        config.update(custom_config)

    # Override config values based on command-line inputs
    if args.logo:
        config["logo"] = args.logo
        config["output"] = f"{args.logo}.svg"

    if args.font and check_file_exist(args.font):
        config["font"] = args.font

    if args.fontsize:
        config["fontSize"] = args.fontsize

    if args.padding:
        config["padding"] = args.padding

    if args.color:
        config["path"]["fill"] = args.color

    if args.output:
        output_path = Path(args.output)
        if output_path.is_dir():
            config["output"] = generate_svg_path(str(output_path), config["logo"])
        elif output_path.suffix.lower() == ".svg":
            config["output"] = str(output_path)

    # Write updated config to temporary .logorc file
    write_yaml_config(config)

    return config


def run_logo_generator(config: Dict[str, Any]) -> None:
    """
    Run the external logo generation tool using the given config.

    Args:
        config (dict): Configuration dictionary containing at least 'output'
    """
    script_dir = Path(get_file_dir())
    cmd_path = script_dir.joinpath("..", "tool", "logo").resolve()
    config_dir = script_dir.joinpath("..", "config").resolve()

    # Execute the external tool
    exit_code = os.system(f'"{cmd_path}" -c "{config_dir}"')
    if exit_code != 0:
        print("Error: Logo generation failed.")
        sys.exit(exit_code)

    # Generate PNG version from SVG
    svg_output = config.get("output")
    if not svg_output:
        raise ValueError("Output path not set in config.")

    svg_path = Path(svg_output)
    if not svg_path.is_absolute():
        svg_path = svg_path.resolve()

    generate_png_with_white_background(str(svg_path), suffix='')
    print(f"✅ Successfully generated logo: {svg_path}")


def main() -> None:
    """Main entry point for the CLI interface."""
    try:
        config = parse_args_and_update_config()
        run_logo_generator(config)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
