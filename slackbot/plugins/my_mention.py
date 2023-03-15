# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import requests

@respond_to('こんにちは'and'こんばんは')
def mention_func(message):
    message.reply('これはテスト返信です') # メンション返信

@respond_to('スケジュール')
def mention_func(message):
    message.reply('これはテスト返信です') # メンション返信

@listen_to('あばば')
def liseten_func(message):
    message.react('+1')

@listen_to('就活')
def listen_fung(message):
    url = "https://slack.com/api/conversations.history"
    token = "xoxb-234972346128-2826231709184-R6ZbOmiAacv3oSLpE45DM0ak"

    header={
        "Authorization": "Bearer {}".format(token)
    }

    payload  = {
        "channel" : "C02N0T4SG2K",
        "limit" : "1",
        "ts" : "latest",
        "inclusive" : True
        }

    res = requests.get(url, headers=header, params=payload)
    message.reply(res.json())