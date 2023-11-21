""" 
-------------------------------------------------------------------
 Telebased Telegram Bot
 Author: @ashirbadsahu
 Github: https://github.com/ashirbadsahu/telebased
 Description: A Telegram bot built using the telebot library for basic messaging and DuckDuckGo API for keyword searches.
 Created on: 16/11/2023
 Setup Instructions:
    1. Clone the repository: git clone https://github.com/mygithubid/telebased.git
    2. Install dependencies: pip install python-dotenv pyTelegramBotAPI
    3. Set up environment variables, including BOT_TOKEN.
    4. Run the bot: python bot.py
 Usage Instructions:
    - /start: Initiates the bot and displays a welcome message.
    - /help: Provides information on available commands and their usage.
    - /g <keyword>: Performs a keyword search using DuckDuckGo API.
    - Any other message: Echoes the received message back.
 License: This project is licensed under the MIT License - see the LICENSE.md file for details.
-------------------------------------------------------------------
"""

# Importing necessary libraries
from dotenv import load_dotenv
import os
import telebot
import requests
import json
import random

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


def duckduckgo_search(query):
    # DuckDuckGo API endpoint
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
    # Sending a welcome message in response to the /start command
    bot.reply_to(message, "Namaste ji 🙏\n/help for usage details")

# Handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/start - to start the bot\n/help - to see available options\n/g <keyword> - to search a keyword")

# Handler for the /g command (keyword search)
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

@bot.message_handler(commands=['true'])
def send_true(message):
    reply = "real" if random.choice([True, False]) else "false"
    bot.reply_to(message, reply)

# Handler for any other messages (echoing the message back)
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Initiating the bot to continuously poll for new messages
bot.infinity_polling()