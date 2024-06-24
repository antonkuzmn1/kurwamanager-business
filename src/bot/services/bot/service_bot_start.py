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
from telegram.ext import ContextTypes


class ServiceBotStart:
    _UPDATE: Update = None
    _CONTEXT: [ContextTypes, any] = None
    _ID: int = None

    def __init__(self, update: Update, context: [ContextTypes, any]) -> None:
        self._UPDATE = update
        self._CONTEXT = context
        self._ID = update.message.from_user.id

    async def entry(self) -> None:
        print(f'start: {self._ID}')
