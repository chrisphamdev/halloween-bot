"""
    This bot was developed by Chris Pham and Wesley Heath (TM).
    This bot was created for the Discord server UoA Esports.
    All enquiries please contact chrisphamdev@gmail.com
    All use of this bot must be approved by its authors.
"""

# import asyncio
# import discord
# from discord.ext.commands import Bot
from discord.ext import commands

# Import the implemented functionalities from different modules
# TODO Create an extension for these commands.
from general_commands.basiccommands import *
from general_commands.reaction_listener import *

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)
