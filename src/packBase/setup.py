#!/usr/bin/env python3
import os
import shutil
import subprocess
from .templates import *
from .utils import *

class PackSetup:
    def __init__(self, package_name='packBase', author='Hanice Sun', email='hanicesun@gmail.com', github_account='HaniceSun'):
        self.package_name = package_name
        self.author = author
        self.email = email
        self.github_https = f'https://github.com/{github_account}'
        self.github_ssh = f'git@github.com:{github_account}'
        print(f'package name: {package_name}')
    
    def make_environment(self, out_file='environment.yml'):
        with open(out_file, 'w') as f:
            f.write(env_template.format(package_name=self.package_name).strip())
        print(f'{out_file} is created')

    def make_pyproject(self, out_file='pyproject.toml'):
        with open(out_file, 'w') as f:
            f.write(pyproject_template.format(package_name=self.package_name,
                                              author=self.author, email=self.email,
                                              github_https=self.github_https).strip())
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

    def make_utils(self, out_file='utils.py', out_dir='src'):
        with open(f'{out_dir}/{self.package_name}/{out_file}', 'w') as f:
            f.write(utils_template.format(package_name=self.package_name).strip())
        print(f'{out_dir}/{self.package_name}/{out_file} is created')

    def make_cli(self, out_file='cli.py', out_dir='src'):
        with open(f'{out_dir}/{self.package_name}/{out_file}', 'w') as f:
            f.write(cli_template.format(package_name=self.package_name).strip())
        print(f'{out_dir}/{self.package_name}/{out_file} is created')

    def make_main(self, out_file='__main__.py', out_dir='src'):
        with open(f'{out_dir}/{self.package_name}/{out_file}', 'w') as f:
            f.write(main_template.format(package_name=self.package_name).strip())
        print(f'{out_dir}/{self.package_name}/{out_file} is created')

    def make_logo(self, out_file='logo.png', logo_dir='assets'):
        os.makedirs(logo_dir, exist_ok=True)
        os.touch(f'{logo_dir}/{out_file}')
        print(f'{out_file} need to be updated')

    def make_readme(self, out_file='README.md'):
        with open(f'{out_file}', 'w') as f:
            f.write(readme_template.format(package_name=self.package_name,
                                           author=self.author, email=self.email).strip())
        print(f'{out_file} need to be updated')

    def make_license(self, out_file='LICENSE'):
        with open(f'{out_file}', 'w') as f:
            f.write(license_template.format(year=datetime.now().year, author=self.author).strip())
        print(f'{out_file} is created')

    def make_gitignore(self, out_file='.gitignore'):
        gitignore_file = f'{BASE}/data/{out_file}'
        shutil.copy(gitignore_file, out_file)

    def make_git(self, git_dir='.git', commit_message='initial commit', github_remote_name='origin'):
        if not os.path.exists(git_dir):
            cmd = 'git config --global init.defaultBranch main; git init'
            subprocess.run(cmd, shell=True, check=True)
        cmd = f'git add .; git commit -m "{commit_message}"'
        subprocess.run(cmd, shell=True)
        print('git repo is created')

        github_remote_url = f'{self.github_ssh}/{self.package_name}.git'
        cmd = f'git remote add {github_remote_name} {github_remote_url}'
        subprocess.run(cmd, shell=True)
        print(f'git remote {github_remote_name} is set to {github_remote_url}')

    def __call__(self):
        self.make_environment()
        self.make_pyproject()
        self.make_requirements()
        self.make_src()
        self.make_utils()
        self.make_cli()
        self.make_main()
        self.make_license()
        print('----------------')
        self.make_logo()
        self.make_readme()
        self.make_gitignore()
        self.make_git()

if __name__ == '__main__':
    package_name = os.path.basename(os.getcwd())
    ps = PackSetup(package_name)
    ps()
