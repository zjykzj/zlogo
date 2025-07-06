# -*- coding: utf-8 -*-

"""
@date: 2020/7/25 下午7:33
@file: setup.py.py
@author: zj
@description:

python setup.py clean --all
rm -rf dist/
python setup.py sdist bdist_wheel
twine upload dist/*

"""

import os
import sys
import shutil
from pathlib import Path
from setuptools import setup, find_packages, Command

# ---------------------- #
# 超参数设置

NAME = "zlogo"
AUTHOR = "zj"
AUTHOR_EMAIL = "wy163zhuj@163.com"
DESCRIPTION = "A simple logo generator that creates SVG and PNG logos from text."
URL = "https://github.com/zjykzj/zlogo"
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = [
    "cairosvg >= 2.5.0",  # 用于SVG转PNG
]
EXTRA_REQUIRE = {
    "dev": ["twine", "wheel", "setuptools"],  # 上传/打包工具
}
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: Apache Software License",
    "Topic :: Multimedia :: Graphics",
    "Intended Audience :: Developers",
]
SOURCE_FOLDER = 'zlogo'
CONSOLE_SCRIPTS = ['zlogo = zlogo.engine.cli:main']


# ---------------------- #


class UploadCommand(Command):
    """Custom command to build and upload the package to PyPI."""
    description = 'Build and publish the package.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def status(msg):
        print(f"\033[1m{msg}\033[0m")

    def run(self):
        here = Path(__file__).parent.resolve()

        self.status("Removing previous builds…")
        dist_dir = here / "dist"
        if dist_dir.exists():
            try:
                shutil.rmtree(dist_dir)
            except Exception as e:
                print(f"Error removing dist directory: {e}")
                sys.exit(1)

        self.status("Building Source and Wheel distribution…")
        # 删除 --universal，避免误导为兼容 Python 2
        # cmd = f"{sys.executable} setup.py sdist bdist_wheel --universal"
        cmd = f"{sys.executable} setup.py sdist bdist_wheel"
        if os.system(cmd) != 0:
            self.status("Build failed.")
            sys.exit(1)

        self.status("Uploading package to PyPI via Twine…")
        if os.system("twine upload dist/*") != 0:
            self.status("Upload failed.")
            sys.exit(1)

        self.status("Pushing git tags…")
        version = get_version()
        if os.system(f"git tag v{version}") != 0 or os.system("git push --tags") != 0:
            self.status("Git tag/push failed.")
            sys.exit(1)

        self.status("Done.")
        sys.exit()


def get_version():
    init_path = Path(__file__).parent / SOURCE_FOLDER / "__init__.py"
    with open(init_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("\"'")
    raise RuntimeError("Version not found in __init__.py")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=get_version(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={
        'zlogo': [
            'tool/logo',
            'config/*.logorc',
        ]
    },
    include_package_data=True,
    classifiers=CLASSIFIERS,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRE,
    entry_points={
        "console_scripts": CONSOLE_SCRIPTS,
    },
    cmdclass={
        "upload": UploadCommand,
    },
)
