from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import TELEGRAM_TOKEN
from src.bot.handlers.handler_callback import handler_callback
from src.bot.handlers.handler_message import handler_message
from src.bot.handlers.handler_start import handler_start


def bot_start():
    APP = Application.builder().token(TELEGRAM_TOKEN).build()

    APP.add_handler(CommandHandler("start", handler_start))
    APP.add_handler(CallbackQueryHandler(handler_callback))
    APP.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler_message))

    print('Bot started')
    APP.run_polling(allowed_updates=Update.ALL_TYPES)
