from telegram import Update
from telegram.ext import ContextTypes


class ServiceBotStart:

    _UPDATE: Update = None
    _CONTEXT: [ContextTypes, any] = None

    _ID: int = None

    def __init__(self, update: Update, context: [ContextTypes, any]) -> None:
        self._UPDATE = update
        self._CONTEXT = context

        self._ID = update.message.from_user.id

        print(f'start: {self._ID}')
