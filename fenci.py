#!/usr/bin/env python3
import sys
import jieba

for line in sys.stdin:
    print(' '.join(jieba.cut(line, cut_all=False)))