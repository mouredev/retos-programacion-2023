#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

parser = argparse.ArgumentParser()

print('uso correcto: python3 jaliagag.py "4 + 5 / 6 - -4"\n')

op = ['+','-','*','/','%']

args = sys.argv[1]
inp = args.split()


def check_string(sth):
    for idx, i in enumerate(inp):
        if idx % 2 == 0:
            try:
                a = int(i)
                if isinstance(a,int):
                    continue
            except:
                return False
        else:
            if i in op:
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    if check_string(inp):
        print('true')
    else:
        print('false')
