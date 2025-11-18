#!/usr/bin/env python3
import argparse
import os
from telegram import Bot


p = argparse.ArgumentParser()
p.add_argument('--image', required=True)
p.add_argument('--text', required=False, default='')
args = p.parse_args()


BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
bot = Bot(BOT_TOKEN)
bot.send_photo(chat_id=CHAT_ID, photo=open(args.image,'rb'), caption=args.text)
print('sent ->', args.image)