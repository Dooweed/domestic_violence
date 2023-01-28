import asyncio
import json

import telegram
from django.conf import settings
from django.core.exceptions import PermissionDenied
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import NetworkError, Forbidden

from bot.models import UsernameId


def parse_update(bot: telegram.Bot, request_token: str, request) -> telegram.Update:
    # noinspection GrazieInspection
    """
            First checks if the request came from Telegram.
            If so, parses telegram update and returns it.
            If not, raises forbidden http error.
        :param telegram.Bot bot: Bot instance
        :param str request_token: Token that was passed in request
        :param request: The actual request
        :return: Telegram update (if token is correct)
        :rtype: telegram.Update
        """
    # Abort request if it is not from telegram
    if bot.token != request_token:
        raise PermissionDenied('Token checking failed')

    # Parse telegram update from json
    update = telegram.Update.de_json(json.loads(request.body), bot)

    return update


def send_message_to_telegram(username, message):
    telegram_id = UsernameId.objects.get(username=username).telegram_id

    async def inner():
        async with Bot(settings.BOT_TOKEN) as bot:
            try:
                await bot.send_message(telegram_id, message, parse_mode=ParseMode.HTML)
            except NetworkError as e:
                print(e)
                await asyncio.sleep(1)
            except Forbidden as e:
                print(e)
                pass

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    loop.run_until_complete(inner())
