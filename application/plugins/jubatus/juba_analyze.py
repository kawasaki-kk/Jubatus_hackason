#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from jubatus.common import Datum

from .juba_abstract import KomachiRecommender
from .services import load_json
from .mecab import get_AllNouns

DATA_FILE_DIR = "../data/"

def recommend_Komachi(content, recommend_num=1, learned_file_name=""):
    # 日報本文を受け取り、出現する名詞とその出現回数のDatumをクエリとして、
    # Jubatus recomenderから類似記事を取得する。
    #
    # content: 日報本文
    # recommend_num: おすすめする記事数
    # learned_file_name: 事前に保存しておいた学習モデルのファイル名
    #
    # return 類似記事のタイトル、類似度スコア、url、tag情報

    # Jubatus recommenderサーバに接続
    recommender = KomachiRecommender()
    if learned_file_name:
        recommender.load(learned_file_name)  # 保存した学習モデルがあれば読み込む

    # 対話履歴からDatum作成
    datum = Datum(get_AllNouns(content))

    # recommend_numで指定した数、類似記事の情報を取得
    similar_komachi_articles\
        = recommender.similar_row_from_datum(datum, recommend_num)

    data = []
    for article in similar_komachi_articles:
        # 類似記事のid＝ファイル名から、類似記事のデータをロード
        # with open("../data/all.json") as f:
        #     all_data = f.readlines()

        #item = load_json(
        #    os.path.join(os.path.dirname(os.path.abspath(__file__)), DATA_FILE_DIR),
        #    article.id)
        
        # データから、各情報をappend
        # data.append({
        #    "title": item["title"],
        #    "score": article.score,
        #    "url": item["url"]
        #    #"tags": item["tags"]
        #})
        data.append(article.id)
    #return data
    return data