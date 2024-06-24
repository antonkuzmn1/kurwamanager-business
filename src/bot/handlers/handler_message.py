import json
from typing import Coroutine, Any

from telegram import Update
from telegram.ext import ContextTypes

from config import TELEGRAM_ID
from src.bot.common.common_type_vars import RT
from src.bot.services.bot.service_bot_message import ServiceBotMessage
from src.bot.services.business.service_business_message import ServiceBusinessMessage


async def handler_message(update: Update, context: [ContextTypes, any]) -> Coroutine[Any, Any, RT]:

    if update.business_message is not None:
        ServiceBusinessMessage(update, context)

    if update.message is not None:
        ServiceBotMessage(update, context)

    return Coroutine[Any, Any, RT]
