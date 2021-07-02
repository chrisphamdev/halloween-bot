"""
    This bot was developed by Chris Pham and Wesley Heath (TM).
    This bot was created for the Discord server UoA Esports.
    All enquiries please contact chrisphamdev@gmail.com
    All use of this bot must be approved by its authors.
"""

# TO RUN THE BOT, RUN THIS FILE
from helper.JsonHelper import JsonHelper
from main import bot
from distest.patches import patch_target

# This patches out bot message checking allows for an external testing bot to run tests.
BOT_TESTING = True

if BOT_TESTING:
    bot = patch_target(bot)

token = JsonHelper.json_read('token.json')

bot.run(token)
