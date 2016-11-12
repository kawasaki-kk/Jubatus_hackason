# -*- coding: utf-8 -*-

import re
from collections import Counter
import MeCab


# Mecabで形態素解析、名詞のみを取得する
def get_AllNouns(text):
    mecab = MeCab.Tagger('')
    mecab.parse('')  # 文字列がGCされるのを防ぐ

    node = mecab.parseToNode(text)
    word = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            # 単語を取得
            word.append(node.surface)
        # 次の単語に進める
        node = node.next
    return extract_Symbols(Counter(word))


# 記号のみの名詞を削除する
def extract_Symbols(dic):
    pattern = "[\W_]"  # 半角英数字（と日本語）と_以外にマッチ
    for key in list(dic.keys()):
        if re.search(pattern, key) is not None:
            del dic[key]
    return dic