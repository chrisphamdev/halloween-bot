# This module handles any reaction_add event

# import discord
# from discord.ext.commands import Bot
# from discord.ext import commands, tasks
# import asyncio
# import time
# from discord import client
from discord.utils import get

from main import bot
# from helper.EmbedCreator import EmbedCreator
import json


@bot.event
async def on_raw_reaction_add(data):
    message_id = None
    with open('config.json', 'r') as file:
        config = json.load(file)
        message_id = config['role_message']

    if data.message_id == message_id:
        # replace this with id of the 'Hunter' role
        role_id = config['role_id']

        if data.emoji.name == '1️⃣':
            role = get(data.member.guild.roles, id=role_id)
            try:
                await data.member.add_roles(role)
            except Exception as e:
                print(e)


@bot.event
async def on_raw_reaction_remove(data):
    message_id = None
    with open('config.json', 'r') as file:
        config = json.load(file)
        message_id = config['role_message']
    
    if data.message_id == message_id:
        # replace this with id of the 'Hunter' role
        role_id = config['role_id']

        if data.emoji.name == '1️⃣':
            guild = bot.get_guild(data.guild_id)
            role = get(guild.roles, id=role_id)
            member = guild.get_member(data.user_id)
            try:
                await member.remove_roles(role)
            except Exception as e:
                print(e)
