# -*- coding: utf-8 -*-
from slackbot.bot import respond_to, listen_to


@listen_to('私は(.*)です')
@listen_to('わたしは(.*)です')
def hello(message, something):
    message.reply('こんにちは!{0}さん。'.format(something))

@respond_to('(.*)')
def refrection(message, something):
    message.reply(something)