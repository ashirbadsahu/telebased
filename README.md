# TELEBASED
 It's a **telegram bot** with various features(currently one).
 ## Commands
 **/start** - to start the bot
 **/help** - to see available options
 **/g <keyword>** - to search a keyword
 

 ## Features
 ### Duckduckgo search
 Uses Duckduckgo's instant answer api.
 `/g keyword` to search keywords.


## Hosting it locally
 1. Clone the repository

    ```
    git clone https://github.com/ashirbadsahu/telebased.git
    ```

 1. Go to Telegram and search `BotFather`
 1. `/newbot` and make a newbot.
 1. Obtain the API TOKEN
 1. make a .env file

    ```
    BOT_TOKEN="YOUR_API_TOKEN"
    ```

    >Replace `YOUR_API_TOKEN` with the token you got.
 1. Install these libraries

    ```
    pip install python-dotenv
    pip install pyTelegramBotAPI
    ```
1. Now run it the bot

    ```
    python bot.py
    ```

Thanks for reading 🙏

