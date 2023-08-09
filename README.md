# uplancebot-public
Telegram bot for job notifications

Add me in telegram: [Uplancebot]

Set a feed url -> Get a messages with new jobs

### How to deploy
Prerequsites: docker, docker-compose

1. Clone repo
2. Create file inside cloned repo `bot.env` contains `BOT_TOKEN=<tg bot token>`
3. Start containers with `docker-compose up -d`. 2 container will start (mongo and uplancebot)
4. Check your bot, try adding new feeds

### Commands

- /start - Start bot
- /add_feed - Add new RSS feed
- /list_feeds - List all RSS feeds
- /delete_feed - Delete RSS feed
- /period - Change period for updates
- /upwork_status_on - Enable Upwork website status
- /upwork_status_off - Disable Upwork website status
- /help - Get help
- /stop - Stop bot

### Todo's

- More options for query
- Change a interval of updates

[Uplancebot]:https://t.me/uplancebot
