from telegram import Update
from telegram.ext import ContextTypes


class ServiceBusinessMessage:

    _UPDATE: Update = None
    _CONTEXT: [ContextTypes, any] = None

    _ID: int = None
    _TEXT: str = None

    def __init__(self, update: Update, context: [ContextTypes, any]) -> None:
        self._UPDATE = update
        self._CONTEXT = context

        self._ID = update.business_message.from_user.id
        self._TEXT = update.business_message.text

        print(f'business: message: {self._ID}: {self._TEXT}')
