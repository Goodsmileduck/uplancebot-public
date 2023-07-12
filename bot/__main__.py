import ssl
import asyncio
import logging
from urllib.parse import urlparse

from aiohttp import web
from config import settings
from bot.main import bot
from bot.tasks import update_process, update_upwork_status
from prometheus_async import aio


async def loop_task(task):
    '''Endless cycle for dataset updating'''
    while True:
        try:
            res = await task()
        except Exception as e:
            logging.warn('Task in loop failed')
            logging.exception(e)
        await asyncio.sleep(settings.MIN_UPDATE_PERIOD)


if __name__ == '__main__':
    asyncio.ensure_future(loop_task(update_process))
    asyncio.ensure_future(loop_task(update_upwork_status))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.delete_webhook())
    bot.run(debug=settings.DEBUG, reload=True)
