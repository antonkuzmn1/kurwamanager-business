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

from typing import Coroutine, Any

from telegram import Update
from telegram.ext import ContextTypes

from src.bot.common.common_type_vars import RT
from src.bot.services.bot.service_bot_message import ServiceBotMessage
from src.bot.services.business.service_business_message import ServiceBusinessMessage


async def handler_message(update: Update, context: [ContextTypes, any]) -> Coroutine[Any, Any, RT]:

    if update.business_message is not None:
        ServiceBusinessMessage(update, context)

    if update.message is not None:
        ServiceBotMessage(update, context)

    return Coroutine[Any, Any, RT]
