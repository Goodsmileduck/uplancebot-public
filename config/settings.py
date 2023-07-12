# Basic settings
import os
from envparse import env

#static
UPWORK_STATUS = 'https://api.status.io/1.0/status/55a1f951d0ef560d6e00006e'
DEBUG = env('DEBUG', cast=bool, default=False)
BOT_TOKEN = env('BOT_TOKEN')
DB_HOST = env('DB_HOST', default='mongo')
DB_PORT = env('DB_PORT', cast=int, default=27017)
DB_NAME = env('DB_NAME', default='uplance')
DB_MAX_POOL_SIZE = env('DB_MAX_POOL_SIZE', cast=int, default=300)
MIN_UPDATE_PERIOD = env('MIN_UPDATE_PERIOD', cast=int, default=10)
MAX_FEED_COUNT =  env('MAX_FEED_COUNT', cast=int, default=3)
GLOBAL_MAX_FEED_COUNT =  env('GLOBAL_MAX_FEED_COUNT', cast=int, default=15)
