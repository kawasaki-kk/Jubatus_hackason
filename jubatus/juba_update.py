# -*- coding: utf-8 -*-

from jubatus.common import Datum
from progressbar import ProgressBar

from juba_abstract import KomachiRecommender
from services import load_json, get_all_files
from mecab import get_AllNouns

DATA_FILE_DIR = "./data/items/"

if __name__ == '__main__':
    # Jubatus recommenderサーバに接続して、
    # DATA_FILE_DIRで指定したディレクトリ内の全ファイル.jsonから
    # keyをファイル名、特徴量をファイルのbodyに出現する名詞とその出現回数の辞書
    # として、サーバにアップロードする

    # サーバに接続
    recommender = KomachiRecommender()

    # DATA_FILE_DIR以下の全ファイル名のリストを取得
    all_files = get_all_files(DATA_FILE_DIR)

    # プログレスバーの設定
    progress = ProgressBar(maxval=len(all_files))

    for i, file_name in enumerate(all_files):
        # 指定したディレクトリ内の全ファイルを読み込んで、
        data = load_json(DATA_FILE_DIR, file_name)
        # print(data["title"])
        datum = Datum(
            get_AllNouns(data["body"])  # body内に出現する名詞と、その出現回数の辞書をDatumとして作成
        )

        # サーバにアップロード
        recommender.update_row(file_name, datum)

        # プログレスバー表示
        progress.update(i + 1)¥