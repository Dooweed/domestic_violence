import asyncio

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update, Bot

from bot.models import UsernameId
from bot.utils import parse_update


@csrf_exempt
def telegram_view(request, bot_token):
    async def inner():
        async with Bot(settings.BOT_TOKEN) as bot:
            update: Update = parse_update(bot, bot_token, request)

            if update.effective_user and update.effective_user.username:
                return update.effective_user.username, update.effective_user.id

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()

    result = loop.run_until_complete(inner())

    if result is not None:
        UsernameId.objects.create(username=result[0], telegram_id=result[1])

    return HttpResponse('gut', status=200)


