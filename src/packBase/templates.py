env_template='''
name: {package_name}
channels:
  - bioconda
  - conda-forge
  - defaults
dependencies:
  - python=3.12.12
  - setuptools=80.9.0
  - numpy=2.4.1
  - pandas=3.0.0
  - matplotlib=3.10.8
  - seaborn=0.13.2
  - pip
  - pip:
      - -r requirements.txt
      - -e .
'''

pyproject_template='''
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "0.0.1"
description = "to be updated"
readme = "README.md"
requires-python = ">=3.12"

authors = [
  {{name = "{author}", email = "{email}"}}
]

[project.urls]
"Homepage" = "{github_https}/{package_name}"

[project.scripts]
{package_name} = "{package_name}.cli:main"

[tool.setuptools.dynamic]
dependencies = {{file = ["requirements.txt"]}}

[tool.setuptools.packages]
find = {{ where = ["src"] }}

[tool.setuptools.package-dir]
"" = "src"

[tool.setuptools.package-data]
{package_name} = ["data/*.txt*", "config/*.yaml"]
'''

requirements_template='''
'''

main_template='''
from .cli import main
if __name__ == "__main__":
    main()
'''

cli_template='''
import argparse

def get_parser():
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter_class)
    subparsers = parser.add_subparsers(dest='command', required=True)

    p1 = subparsers.add_parser('train', help='train')
    p1.add_argument('--input', type=str, default=None, help='input data')

    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.command == 'train':
        pass
'''

readme_template='''
<p align="left">
<img src="assets/logo.png" alt="logo" width="200"/>
</p>

## Overview

packBase is a template repository for creating new Python packages.

## Installation

```
git clone git@github.com:HaniceSun/{package_name}.git
conda env create -f environment.yaml
conda activate {package_name}
```

## Usage

```
{package_name} --help
```

## Author and License

**Author:** {author}

**Email:** {email}

**License:** [MIT License](LICENSE)
'''

license_template='''
MIT License

Copyright (c) 2025 {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
