# -*- coding: utf-8 -*-

from telethon.sync import TelegramClient
from data import *
import logging
import getpass

logging.basicConfig(level=logging.INFO)

if api_id == '' or api_hash == '':
    logging.fatal("You must assign a API before using this script! 在登录前你必须给定ID和HASH @ data.py")

logging.info("Trying to Login to Telegram... 正在尝试登录...")
client = TelegramClient('session_file', api_id, api_hash)

client.connect()
if client.is_user_authorized() is not True:
    logging.info('You have not login yet, Trying to log you in... 没有活跃的登录Session，尝试登录...')
    logging.info(
        'if you have 2FA password, please input right now. This Password will not be stored. Otherwise, please press the Enter Key | 如果你有两步验证密码，请现在输入。这个密码不会被保存。否则请直接回车')
    password = getpass.getpass()
    if password != '':
        client.start(password=password)
    else:
        client.start()
