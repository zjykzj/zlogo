# zlogo

![](./imgs/zlogo.png)

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org) [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

> 自定义LOGO

```
# 生成logo文本`hahaha`
$ zlogo -l hahaha
# 指定字体大小为100
$ zlogo -fs 100
# 指定四周空白填充大小为100
$ zlogo -p 100
# 指定输出路径
$ zlogo -o ./zlogo.svg
# 指定配置文件路径
$ zlogo -c ~/zlogo/configs/readme.yaml
```

## 内容列表

- [zlogo](#zlogo)
  - [内容列表](#内容列表)
  - [背景](#背景)
  - [安装](#安装)
  - [使用](#使用)
  - [主要维护人员](#主要维护人员)
  - [致谢](#致谢)
  - [参与贡献方式](#参与贡献方式)
  - [许可证](#许可证)

## 背景

想要设计个人`logo`，找了很多资料，发现

1. [logo.svg](https://github.com/bubkoo/logo.svg)可以自定义`logo`图案，并且能够生成`svg`文件
2. [svglib](https://github.com/deeplook/svglib)可以转换`svg`到`png`
  
写了这个脚本，方便大家使用

## 安装

```
$ pip install zlogo
```

## 使用

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

可以通过命令行参数进行配置，也可以通过配置文件

* `-l`：Logo文本名
* `-f`：使用字体文件（`.ttf`）路径
* `-fs`：字体大小
* `-p`：四周空白填充大小
* `--color`：字体颜色
* `-c`：配置文件（`yaml`）路径
* `-o`：输出图像（`.svg`）路径

关于配置文件，可参考`configs`目录下的`avatar.yaml`和`readme.yaml`

关于字体文件

1. 如果使用参数`-f`指定，必须指定确切路径
2. 如果使用配置文件指定，可以将字体文件放置在`~/.fonts`目录下，在配置文件中指定字体文件名即可

**注意：命令行参数的设置会覆盖配置文件**

## 主要维护人员

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## 致谢

* [bubkoo/logo.svg](https://github.com/bubkoo/logo.svg)
* [deeplook/svglib](https://github.com/deeplook/svglib)
* [Google Noto Fonts](https://www.google.com/get/noto/)

## 参与贡献方式

欢迎任何人的参与！打开[issue](https://gitee.com/zjykzj/zlogo/issues)或提交合并请求。

注意:

* `GIT`提交，请遵守[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)规范
* 语义版本化，请遵守[Semantic Versioning 2.0.0](https://semver.org)规范
* `README`编写，请遵守[standard-readme](https://github.com/RichardLitt/standard-readme)规范

## 许可证

[Apache License 2.0](LICENSE) © 2020 zjykzj