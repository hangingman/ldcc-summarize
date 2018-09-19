# -*- coding: utf-8 -*-
#
"""Livedoor ニュースコーパスから本文、要約のペアを生成する
"""

import argparse
import os
import re

# ファイル名規則
# text/[category]/[category]-[num+].txt
# これ以外に各カテゴリディレクトリにLICENSE.txtがある
#
# コンテンツ規則
# 1: URL
# 2: datetime
# 3: abstract
# 4+: article
#
# "【.*】"は削除したほうが良さそう

def read_file(path):
    with open(path, 'r') as f:
        url = next(f)
        timestamp = next(f)
        abstract = next(f)[:-1]
        article = ''
        for line in f:
            article += line[:-1]
    return url, timestamp, abstract, article

def get_dirs(path):
    dirs = []
    for p in os.listdir(path):
        d = os.path.join(path, p)
        if os.path.isdir(d):
            dirs.append(d)
    return dirs

text_pattern = re.compile('[a-z-]+-\d+.txt')

def get_files(path):
    files = []
    for n in os.listdir(path):
        if text_pattern.fullmatch(n):
            files.append(n)
    return files

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--input_dir', type=str, default="text")
    p.add_argument('--output_article', type=str, default='article.txt')
    p.add_argument('--output_abstract', type=str, default='abstract.txt')
    args = p.parse_args()
    return args

def main():
    args = get_args()
    # fname = "/home/knok/nlp/livedoor-news-corpus/text/it-life-hack/it-life-hack-6918825.txt"
    # print(read_file(fname))
    #print(get_dirs('text'))
    print(get_files('text/it-life-hack'))

if __name__ == '__main__':
    main()