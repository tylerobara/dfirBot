#!/usr/bin/env python3
"""
dfirBot - A Mattermost bot for DFIR triage and incident response
"""

from mmpy_bot import Bot, Settings
from dfirBot import DfirBot
import os
import json

#config = json.load(open('src/config/config.json'))
config = json.load(open('/bot/config/config.json', encoding='utf-8'))

bot = Bot(
    settings=Settings(
        MATTERMOST_URL = config["mattermost"]["url"],
        MATTERMOST_PORT = 80,
        MATTERMOST_API_PATH = '/api/v4',
        BOT_TOKEN = config["mattermost"]["bot"]["token"],
        BOT_TEAM = config["mattermost"]["bot"]["team"],
        SSL_VERIFY = False,
    ),
    plugins=[DfirBot()],
)

bot.run()
