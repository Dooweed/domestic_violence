import asyncio

from telegram import Bot

from domestic_violence import settings

URL = 'https://7035-84-54-86-133.ngrok.io'

async def main():
    async with Bot(settings.BOT_TOKEN) as bot:
        url = URL + f'/bot/{settings.BOT_TOKEN}/'
        print(await bot.set_webhook(url))


try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
loop.run_until_complete(main())
