# This bot was developed by Chris Pham and Wesley Heath (TM).
# This bot was created for the Discord server UoA Esports.
# All enquiries please contact chrisphamdev@gmail.com
# All use of this bot must be approved by its authors.


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

# Import the implemented functionalities from different modules
from general_commands.basiccommands import *
from general_commands.reaction_listener import *
