""" 
-------------------------------------------------------------------
 Telebased Telegram Bot
 Author : @ashirbadsahu
 Github : https://github.com/ashirbadsahu/telebased
 Created on : 16/11/2023
-------------------------------------------------------------------
 """
from dotenv import load_dotenv
import os
import telebot
import requests
import json

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def duckduckgo_search(query):
    endpoint = 'https://api.duckduckgo.com/'
    params = {
        'q': query,
        'format': 'json'
    }
    response = requests.get(endpoint, params=params)
    search_results = json.loads(response.text)
    return search_results

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaste ji 🙏\n/help for usage details")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/start - to start the bot\n/help - to see available options\n/g <keyword> - to search a keyword")


@bot.message_handler(commands=['g'])
def send_gogl(message):
    if message.reply_to_message and message.reply_to_message.from_user.is_bot:
        query = message.text
    else:
        query = message.text[3:]
    search_results = duckduckgo_search(query)
    if search_results['RelatedTopics']:
        reply = search_results['RelatedTopics'][0]['Text']
    else:
        reply = "No results found"
    bot.reply_to(message, reply)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()