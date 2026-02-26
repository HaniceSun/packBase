#!/usr/bin/env python3
import os
import subprocess
from templates import *

class PackConfig:
    def __init__(self, package_name):
        self.package_name = package_name
        print(f'package name: {package_name}')
    
    def make_environment(self, out_file='environment.yml'):
        with open(out_file, 'w') as f:
            f.write(env_template.format(package_name=self.package_name).strip())
        print(f'{out_file} is created')

    def make_pyproject(self, out_file='pyproject.toml'):
        with open(out_file, 'w') as f:
            f.write(pyproject_template.format(package_name=self.package_name).strip())
        print(f'{out_file} is created')

    def make_requirements(self, out_file='requirements.txt'):
        with open(out_file, 'w') as f:
            f.write(requirements_template.format(package_name=self.package_name).strip())
        print(f'{out_file} is created')

    def make_src(self, out_dir='src', sub_dir=['data', 'config']):
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        if not os.path.exists(f'{out_dir}/{self.package_name}'):
            os.mkdir(f'{out_dir}/{self.package_name}')
        for _dir in sub_dir:
            if not os.path.exists(f'{out_dir}/{self.package_name}/{_dir}'):
                os.mkdir(f'{out_dir}/{self.package_name}/{_dir}')
        print(f'{out_dir} is created')
        for _dir in sub_dir:
            print(f'{out_dir}/{self.package_name}/{_dir} is created')

    def make_cli(self, out_file='cli.py', out_dir='src'):
        with open(f'{out_dir}/{self.package_name}/{out_file}', 'w') as f:
            f.write(cli_template.format(package_name=self.package_name).strip())
        print(f'{out_dir}/{self.package_name}/{out_file} is created')

    def make_main(self, out_file='__main__.py', out_dir='src'):
        with open(f'{out_dir}/{self.package_name}/{out_file}', 'w') as f:
            f.write(main_template.format(package_name=self.package_name).strip())
        print(f'{out_dir}/{self.package_name}/{out_file} is created')

    def make_logo(self, out_file='logo.png'):
        print(f'{out_file} need to be updated')

    def make_readme(self, out_file='README.md'):
        print(f'{out_file} need to be updated')

    def make_license(self, out_file='LICENSE'):
        print('update {out_file} if needed')

    def make_gitignore(self, out_file='.gitignore'):
        print('update .gitignore if needed')

    def update_git_remote(self, remote_name='origin', account='git@github.com:HaniceSun'):
        if self.package_name != 'packBase':
            remote_url = f'{account}/{self.package_name}.git'
            cmd = f'git remote set-url {remote_name} {remote_url}'
            subprocess.run(cmd, shell=True, check=True)
            print(f'git remote {remote_name} is updated to {remote_url}')

    def __call__(self):
        self.make_environment()
        self.make_pyproject()
        self.make_requirements()
        self.make_src()
        self.make_cli()
        self.make_main()
        self.make_license()
        print('----------------')
        self.make_logo()
        self.make_readme()
        self.make_gitignore()
        self.update_git_remote()

if __name__ == '__main__':
    package_name = os.path.basename(os.getcwd())
    pc = PackConfig(package_name)
    pc()
