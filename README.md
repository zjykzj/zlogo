<div align="center"><a title="" href="https://github.com/zjykzj/zlogo"><img align="center" src="./imgs/zlogo.svg"></a></div>

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

***Update in 2025***

*[Kozea/CairoSVG](https://github.com/Kozea/CairoSVG?tab=readme-ov-file) is better suited for use with **zlogo** compared to `svglib`.*

## Install

```
$ pip install zlogo
```

## Usage

```
# Generate a logo with the text "hahaha"
$ zlogo -l hahaha

# Specify the font size as 100
$ zlogo -fs 100

# Set padding around the logo to 100 pixels
$ zlogo -p 100

# Define the output file path
$ zlogo -o ./zlogo.svg

# Use a configuration file to customize the logo
$ zlogo -c ~/zlogo/configs/readme.yaml
```

### 📁 Configuration File

* For available configuration options, please refer to the example files: `avatar.yaml` and `readme.yaml` in the `configs/` directory.
* Command-line arguments **take precedence over** settings in the configuration file.

### 🔤 Font Files

There are two ways to specify a custom font:

1. **Using the `-f` parameter**
    ```shell
    # You must provide the full path to a .ttf (TrueType) font file
    $ zlogo -f /path/to/your/font.ttf
    ```
2. **Using a configuration file**
 
    Place your font file in the `~/.fonts/` directory, and then specify only the filename (not the full path) in the configuration file.

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