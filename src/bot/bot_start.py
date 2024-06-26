"""

Copyright 2024 Anton Kuzmin (https://github.com/antonkuzmn1)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

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
