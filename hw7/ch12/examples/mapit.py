#!/usr/bin/env python
# mapIt.py - Lauches a map in the browser using an address from then
# command line/clipboard.


import webbrowser
import sys
import argparse

# takes what is passed to the script and access it to become a name space
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('address')

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    print('The given address:', args.address)

    webbroswer.open(
        'http://www.google.com/maps/place/' + args.address
    )


if __name__ == '__main__':
    main()
