import argparse
import os
from .setup import PackSetup

def get_parser():
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter_class)
    parser.add_argument('--package', type=str, default=None, help='package name, using the current directory name if not specified')
    parser.add_argument('--author', type=str, default='Hanice Sun', help='author name')
    parser.add_argument('--email', type=str, default='hanicesun@gmail.com', help='email address')
    parser.add_argument('--github_account', type=str, default='HaniceSun', help='github account')
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    package_name = args.package
    if package_name is None:
        package_name = os.path.basename(os.getcwd())
    ps = PackSetup(package_name=package_name, author=args.author, email=args.email, github_account=args.github_account)
    ps()
