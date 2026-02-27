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
