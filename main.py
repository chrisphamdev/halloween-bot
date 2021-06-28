"""
    This bot was developed by Chris Pham and Wesley Heath (TM).
    This bot was created for the Discord server UoA Esports.
    All enquiries please contact chrisphamdev@gmail.com
    All use of this bot must be approved by its authors.
"""

import asyncio
# from discord.ext.commands import Bot
import discord
from discord.ext import commands
from config.ConfigHelper import ConfigHelper

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

# Initialise ConfigHelper object and attach it to the bot.
config_helper = ConfigHelper()
bot.config_helper = config_helper


@bot.event
async def on_ready():
    # Future extensions will be called here.
    bot.load_extension('cogs.admin_commands')
    bot.load_extension('cogs.reaction_listener')
    print('Halloween Bot has been deployed.')
