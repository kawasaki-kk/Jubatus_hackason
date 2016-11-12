# -*- coding: utf-8 -*-
import sys

from jubatus.common import Datum
from progressbar import ProgressBar
import json

from juba_abstract import KomachiRecommender
from mecab import get_AllNouns

DATA_FILE_DIR = "../data/"
#sys.path.append(DATA_FILE_DIR)


if __name__ == '__main__':
    # Jubatus recommenderサーバに接続して、
    # DATA_FILE_DIRで指定したディレクトリ内の全ファイル.jsonから
    # keyをファイル名、特徴量をファイルのbodyに出現する名詞とその出現回数の辞書
    # として、サーバにアップロードする

    # サーバに接続
    recommender = KomachiRecommender()

    # DATA_FILE_DIR以下の全ファイル名のリストを取得
    with open(DATA_FILE_DIR+"all.json") as f:
        all_files = f.readlines()

    # プログレスバーの設定
    progress = ProgressBar(maxval=len(all_files))

    for i, json_file in enumerate(all_files):
        # 指定したディレクトリ内の全ファイルを読み込んで、
        data = json.loads(json_file)
        # print(data["title"])
        datum = Datum(
            get_AllNouns(data["message"])  # body内に出現する名詞と、その出現回数の辞書をDatumとして作成
        )

        # サーバにアップロード
        recommender.update_row(data["title"], datum)

        # プログレスバー表示
        progress.update(i + 1)