from telegram import Update
from telegram.ext import ContextTypes


class ServiceBotCallback:

    _UPDATE: Update = None
    _CONTEXT: [ContextTypes, any] = None

    _ID: int = None
    _DATA: str = None

    def __init__(self, update: Update, context: [ContextTypes, any]) -> None:
        self._UPDATE = update
        self._CONTEXT = context

        self._ID = update.callback_query.from_user.id
        self._DATA = update.callback_query.data

        print(f'callback: {self._ID}: {self._DATA}')
