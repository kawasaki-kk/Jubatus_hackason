# -*- coding: utf-8 -*-
import os
import sys
from slackbot.bot import respond_to, listen_to

# sys.path.append( "../../jubatus/" )
from .jubatus.juba_analyze import recommend_Komachi

class Reply:
    def __init__(self):
        self.counter = 0

    def increase(self):
        self.counter += 1
        return self.counter
r = Reply()

@listen_to('(.*)')
def refrection(message, something):
    count = r.increase()
    if count % 1 == 0:
        #count = str(count)
        #message.reply(count)
        recommend = recommend_Komachi(something)
        print(recommend)
        # print(recommend.url)
        message.reply(recommend[0]['title'])
        message.reply(recommend[0]['url'])
    else:
        message.reply('それで？')