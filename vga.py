#!/usr/bin/env python3

import sys

for line in sys.stdin:
    b = line.encode('utf-8')
    for byte in b:
        num = "00{:0>3b}{:0>3b}{:0>8b}".format(0x0,0x7,byte)
        print(num, end='')
    for _ in range(80-len(b)):
        num = "00{:0>3b}{:0>3b}{:0>8b}".format(0x0,0x7,0x20)
        print(num, end='')
