# -*- encoding: utf-8 -*-

import dns.query
import argparse

__version__ = "0.0.1"


def main():
    print('WIP Parallel DNS Bruteforce')
    parser = argparse.ArgumentParser(
        version=__version__,
        description='brutedns - Parallel DNS (CNAME) Bruteforce Tool',
        epilog='Use responsibly, Enjoy pentesting'
    )

    parser.add_argument(
        '-w',
        '--wordlist',
        dest='wordlist',
        action='store',
        help='newline separated wordlist. Eg: github-dorks.txt'
    )

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
