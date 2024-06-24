from typing import Coroutine, Any

from telegram import Update
from telegram.ext import ContextTypes

from src.bot.common.common_type_vars import RT
from src.bot.services.bot.service_bot_callback import ServiceBotCallback


async def handler_callback(update: Update, context: [ContextTypes, any]) -> Coroutine[Any, Any, RT]:

    ServiceBotCallback(update, context)

    return Coroutine[Any, Any, RT]
