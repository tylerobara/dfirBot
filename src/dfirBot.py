#!/usr/bin/env python3

from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message
from datetime import datetime

import requests
import os
import click
import subprocess
import random
import time
import json

config = json.load(open('/bot/config/config.json', encoding='utf-8'))
#config = json.load(open('src/config/config.json'))
hiveUrl = config["thehive"]["url"]
hiveKey = config["thehive"]["key"]

headers = {
    'Authorization': f"Bearer {hiveKey}"
}

def get_icon(severity):
    if severity == 1:
        return "\U0001F7E2"
    elif severity == 2:
        return "\U0001F7E1"
    elif severity == 3:
        return "\U0001F7E0"
    elif severity == 4:
        return "\U0001F534"
    else:
        return "ERROR!"

def get_cases():
    """
    Get the cases from TheHive
    """
    response = requests.get(f"{hiveUrl}/api/case", headers=headers, timeout=5)
    print(hiveUrl)
    print(hiveKey)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def case_table(cases):
    """
    Create a markdown table of cases
    """
    table = """
| Case ID | Severity | Title | Description |
| --- | --- | --- | --- |
    """
    for case in cases:
        table += f"| {case['caseId']} | {get_icon(case['severity'])} | {case['title']} | {case['description'][0:60]} |\n"
    return table

class DfirBot(Plugin):
    """
    A simple bot that responds to messages.
    """
    @listen_to("hello", needs_mention=True)
    async def wake_up(self, message: Message):
        """
        Respond to a user that says hello.
        """
        reply = ( 
            f"Hello {message.sender_name}\n"
        )
        self.driver.reply_to(message, reply)

    @listen_to("help", needs_mention=True)
    async def help(self, message: Message):
        """
        Provide a list of commands that dfirBot understands
        """
        reply = (
            f"Help is on the way {message.sender_name}\n"
        )
        self.driver.reply_to(message, reply)

    @listen_to("cases", needs_mention=True)
    async def cases(self, message: Message):
        """
        Provide a list of cases from TheHive
        """
        print(get_cases())
        reply = case_table(get_cases())
        self.driver.reply_to(message, reply)

    @listen_to("remove", needs_mention=True)
    @click.command(help="An example click command with various arguments.")
    @click.argument("POSITIONAL_ARG", type=str)
    @click.option("--keyword-arg", type=str, default='linux', help="A keyword arg.")
    @click.option("-f", "--flag", is_flag=True, help="Can be toggled.")
    def remove_click(
        self, message: Message, positional_arg: str, keyword_arg: float, flag: bool
    ):
        response = "something"
        self.driver.reply_to(message, response)
