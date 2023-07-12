from . import base
from .period import period
from .feed import add_feed, delete_feed, list_feeds


def register_commands(bot):
    '''Registering commands'''

    for cmd in ('start', 'stop', 'help', 'upwork_status_off', 'upwork_status_on'):
        bot.add_command('/{}'.format(cmd), getattr(base, cmd))

    for cmd in ('add_feed', 'delete_feed', 'list_feeds', 'period',
                'stats'):
        bot.add_command('/{}'.format(cmd), eval(cmd))
