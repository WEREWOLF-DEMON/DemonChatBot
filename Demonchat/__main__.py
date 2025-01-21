import sys
import asyncio
import importlib
from flask import Flask
import threading
import config
from Demonchat import ID_CHATBOT
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from Demonchat import LOGGER, Demonchat, userbot, load_clone_owners
from Demonchat.modules import ALL_MODULES
from Demonchat.modules.Clone import restart_bots
from Demonchat.modules.Id_Clone import restart_idchatbots

async def anony_boot():
    try:
        await Demonchat.start()
        try:
            await Demonchat.send_message(int(OWNER_ID), f"**{Demonchat.mention} Is started✅**")
        except Exception as ex:
            LOGGER.info(f"@{Demonchat.username} Started, please start the bot from owner id.")
    
        asyncio.create_task(restart_bots())
        print("Restarting all cloned botsbin background")
        asyncio.create_task(restart_idchatbots())
        print("Restarting all id chatbot in background")
        await load_clone_owners()
        if config.STRING1:
            try:
                await userbot.start()
                try:
                    await Demonchat.send_message(int(OWNER_ID), f"**Id-Chatbot Also Started✅**")
                except Exception as ex:
                    LOGGER.info(f"@{Demonchat.username} Started, please start the bot from owner id.")
    
            except Exception as ex:
                print(f"Error in starting id-chatbot :- {ex}")
                pass
    except Exception as ex:
        print(f"Error in starting Bot:- {ex}")

    for all_module in ALL_MODULES:
        importlib.import_module("Demonchat.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    
    try:
        await Demonchat.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Get the help menu"),
                BotCommand("clone", "Make your own chatbot"),
                BotCommand("idclone", "Make your id-chatbot"),
                BotCommand("cloned", "Get List of all cloned bot"),
                BotCommand("ping", "Check if the bot is alive or dead"),
                BotCommand("lang", "Select bot reply language"),
                BotCommand("chatlang", "Get current using lang for chat"),
                BotCommand("resetlang", "Reset to default bot reply lang"),
                BotCommand("id", "Get users user_id"),
                BotCommand("stats", "Check bot stats"),
                BotCommand("gcast", "Broadcast any message to groups/users"),
                BotCommand("chatbot", "Enable or disable chatbot"),
                BotCommand("status", "Check chatbot enable or disable in chat"),
                BotCommand("shayri", "Get random shayri for love"),
                BotCommand("ask", "Ask anything from chatgpt"),
                BotCommand("repo", "Get chatbot source code"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")
    
    LOGGER.info(f"@{Demonchat.username} Started.")
    
    await idle()


app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping Demonchat Bot...")
