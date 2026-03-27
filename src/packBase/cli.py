import argparse
import os
import subprocess
from .setup import PackSetup

def get_parser():
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter_class)
    subparsers = parser.add_subparsers(dest='command', required=True)

    p1 = subparsers.add_parser("init", help="initialize a new package")
    p1.add_argument('--package', type=str, default=None, help='package name, using the current directory name if not specified')
    p1.add_argument('--author', type=str, default='Hanice Sun', help='author name')
    p1.add_argument('--email', type=str, default='hanicesun@gmail.com', help='email address')
    p1.add_argument('--account', type=str, default='HaniceSun', help='github account')

    p2 = subparsers.add_parser("fresh", help="delete all history and keep only current files for a github repo; internal use only; use with caution!")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.command == 'init':
        package_name = args.package
        if package_name is None:
            package_name = os.path.basename(os.getcwd())
        ps = PackSetup(package_name=package_name, author=args.author, email=args.email, github_account=args.account)
        ps()
    elif args.command == 'fresh':
        choice = input("The repo has been backed up? (yes/NO) ")
        if choice.lower() != 'yes':
            print("Please backup the repo before running this command.")
            return
        cmd = 'git checkout --orphan new-main && git add -A && git commit -m "fresh start" && git branch -D main && git branch -m main && git push -f origin main'
        subprocess.run(cmd, shell=True)
