import logging
from datetime import timedelta
from bot.database import db
from bot.schemas import DefaultChatSchema
from .feed import add_feed

help_msg = '''
Usage:
/start - Start bot
/add_feed - Add new RSS feed
/list_feeds - List all RSS feeds
/delete_feed - Delete RSS feed
/period - Change period for updates
/upwork_status_on - Enable Upwork website status
/upwork_status_off - Disable Upwork website status
/help - Get help
/stop - Stop bot
'''


async def start(chat, msg):
    chat.bot.set_next_step(chat, add_feed)
    await chat.send_text('Bot started.\n'
                         'You can track you jobs using RSS feeds.\n'
                         'You can add multiple feeds.\n'
                         'Let\'s start with first feed. Please send a name for it.\n'
                         '*For example:* main', parse_mode='Markdown')

async def stop(chat, msg):
    await db.chats.delete_many({'chat_id': chat.id})
    return await chat.send_text('Bot stopped.')


async def upwork_status_off(chat, msg):
    d = await db.chats.find_one({'chat_id': chat.id})
    if d is None:
        return await chat.send_text("You don't have subscription, please add it with command /upwork_status_on.")
    await db.chats.update_one({'chat_id': chat.id},
                              {'$set': {'status_notify': False}})
    return await chat.send_text('Upwork status notifications are disabled.')

async def upwork_status_on(chat, msg):
    await db.chats.update_one({'chat_id': chat.id},
                              {'$set': {'status_notify': True}}, upsert=True)
    return await chat.send_text('Upwork status notifications are enabled.')

async def help(chat, msg):
    return await chat.send_text(help_msg)
