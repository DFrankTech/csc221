#!/usr/bin/env python3
''' Mulitplication table maker

Author: demifranklin
'''
import argparse

def create_multiplication_table(N):
    for i in range(1, 11):


    # Place your solution in this function

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', help='size of multiplication table')

    args = parser.parse_args()

    create_multiplication_table(args.N)

if __name__=='__main__':
    main()
