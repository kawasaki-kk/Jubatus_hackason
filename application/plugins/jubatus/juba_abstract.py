# -*- coding: utf-8 -*-

from jubatus.recommender.client import Recommender


SERVER_IP = "127.0.0.1"
SERVER_PORT = 9199
NAME = "recommender_komachi"


class KomachiRecommender(Recommender):
    def __init__(self, host=SERVER_IP, port=SERVER_PORT, name=NAME):
        Recommender.__init__(self, host=host, port=port, name=name)
