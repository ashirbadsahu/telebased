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

# Loading environment variables from a .env file
load_dotenv()

# Retrieving the Bot Token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Creating a TeleBot instance using the provided Bot Token
bot = telebot.TeleBot(BOT_TOKEN)

# Function to perform a DuckDuckGo search
def duckduckgo_search(query):
    # DuckDuckGo API endpoint
    endpoint = 'https://api.duckduckgo.com/'
    
    # Parameters for the API request
    params = {
        'q': query,
        'format': 'json'
    }
    
    # Making a GET request to the DuckDuckGo API
    response = requests.get(endpoint, params=params)
    
    # Parsing the JSON response
    search_results = json.loads(response.text)
    
    # Returning the search results
    return search_results

# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Sending a welcome message in response to the /start command
    bot.reply_to(message, "Namaste ji 🙏\n/help for usage details")

# Handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    # Sending help information in response to the /help command
    bot.reply_to(message, "/start - to start the bot\n/help - to see available options\n/g <keyword> - to search a keyword")

# Handler for the /g command (keyword search)
@bot.message_handler(commands=['g'])
def send_gogl(message):
    # Extracting the search query from the message
    if message.reply_to_message and message.reply_to_message.from_user.is_bot:
        query = message.text
    else:
        query = message.text[3:]
    
    # Performing DuckDuckGo search
    search_results = duckduckgo_search(query)
    
    # Checking if there are related topics in the search results
    if search_results['RelatedTopics']:
        # Extracting the text of the first related topic
        reply = search_results['RelatedTopics'][0]['Text']
    else:
        # If no results found
        reply = "No results found"
    
    # Sending the search results as a reply
    bot.reply_to(message, reply)

# Handler for any other messages (echoing the message back)
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # Echoing the received message back
    bot.reply_to(message, message.text)

# Initiating the bot to continuously poll for new messages
bot.infinity_polling()