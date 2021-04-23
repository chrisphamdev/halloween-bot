# This module contains all basic commands of the bot

import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import asyncio
import time
from discord import client

from main import bot
from helper.EmbedCreator import EmbedCreator


# Custom help message - to be done
bot.remove_command('help')


# Replace default help command to this one.
@bot.command()
async def help(ctx):
    await ctx.send('The rule-set can be accessed here.')
    # TO BE ADDED: GAME RULE


@bot.event
async def on_ready():
    print('Halloween Bot has been deployed.')


# bot info
@bot.command()
async def info(ctx):
    info_str = 'This bot was created by Wesley Heath and Chris Pham for the UoA Esports server. Any feedback will be ' \
           'appreciated. '
    embed = EmbedCreator('Halloween Bot', 'Information', info_str, 'Powered by UoA Esports.')
    await ctx.send(embed=embed.get_embed())


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! This message took {round(bot.latency * 1000)}ms to respond.')