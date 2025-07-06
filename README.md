<!-- <div align="right">
  Language:
    🇺🇸
  <a title="Chinese" href="./README.zh-CN.md">🇨🇳</a>
  <!-- <a title="俄语" href="../ru/README.md">🇷🇺</a> -->
</div>

 <div align="center"><a title="" href="https://github.com/zjykzj/zlogo"><img align="center" src="./imgs/zlogo.png"></a></div> -->

<p align="center">
  «zlogo» allows you to input text to generate logo images
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
  <a href="https://pypi.org/project/zlogo/"><img src="https://img.shields.io/badge/PYPI-ZLOGO-brightgreen"></a>
</p>

Generate logo from text and obtain SVG and PNG format files simultaneously.

Implementation examples are as follows:

```
# generate logo `hahaha`
$ zlogo -l hahaha
# specifies that the font size is 100
$ zlogo -fs 100
# specifies that the surrounding blank fill size is 100
$ zlogo -p 100
# specify the output path
$ zlogo -o ./zlogo.svg
# specify the configuration file path
$ zlogo -c ~/zlogo/configs/readme.yaml
```

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [Contributing](#contributing)
- [License](#license)

## Background

I want to design a personal logo. After find a lot of information, found that

1. [logo.svg](https://github.com/bubkoo/logo.svg) can customize logo patterns and generate svg files
2. [svglib](https://github.com/deeplook/svglib) can convert svg to png
  
So i wrote this script for everyone's convenience

***### Update in 2025***

***[Kozea/CairoSVG](https://github.com/Kozea/CairoSVG?tab=readme-ov-file) is better suited for use with **zlogo** compared to `svglib`.***

## Install

```
$ pip install zlogo
```

## Usage

```
$ zlogo --help
usage: zlogo [-h] [-l LOGO] [-f FONT] [-fs FontSize] [-p PADDING]
             [--color COLOR] [-c CONFIG_FILE] [-o OUTPUT] [-v]

custom logo - ZLOGO

optional arguments:
  -h, --help            show this help message and exit
  -l LOGO, --logo LOGO  specify the logo text
  -f FONT, --font FONT  path to a font file(.ttf)
  -fs FontSize, --fontsize FontSize
                        specify the font size
  -p PADDING, --padding PADDING
                        specify the border size
  --color COLOR         sepcify the text' color
  -c CONFIG_FILE, --config_file CONFIG_FILE
                        path to config file
  -o OUTPUT, --output OUTPUT
                        path to output file(.svg)
  -v, --version         output version infomation
```

It can be configured through command line parameters or through configuration files

* For configuration files, please refer to `avatar.yaml` and `readme.yaml` in the `configs` directory
* For font files
  1. If you specify with the parameter `-f`, you must specify the exact path
  2. If you use the configuration file to specify, you can put the font file in the ` ~/.fonts ` directory and specify the font file name in the configuration file

**Note: the setting of command line parameters overwrites the configuration file**

## Maintainers

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## Thanks

* [bubkoo/logo.svg](https://github.com/bubkoo/logo.svg)
* [deeplook/svglib](https://github.com/deeplook/svglib)
* [Google Noto Fonts](https://www.google.com/get/noto/)
* [vercel/pkg](https://github.com/vercel/pkg)
* [Kozea/CairoSVG](https://github.com/Kozea/CairoSVG?tab=readme-ov-file)

## Contributing

Anyone's participation is welcome! Open an [issue](https://github.com/zjykzj/zlogo/issues) or submit PRs.

## License

[Apache License 2.0](LICENSE) © 2020 zjykzj