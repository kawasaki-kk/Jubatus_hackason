# -*- coding: utf-8 -*-
import os
import sys
from slackbot.bot import respond_to, listen_to

# sys.path.append( "../../jubatus/" )
from jubatus.juba_analyze import recommend_Komachi

class Reply:
    def __init__(self):
        self.counter = 0

    def increase(self):
        self.counter += 1
        return self.counter
r = Reply()
statements = []

@listen_to('(.*)')
def refrection(message, something):
    statements.append(something)
    count = r.increase()
    if count % 5 == 0:
        recommend = recommend_Komachi(statements)
        print(recommend)
        message.reply(*recommend)
    else:
        message.reply('それで？')