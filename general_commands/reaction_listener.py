# This module handles any reaction_add event

import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import asyncio
import time
from discord import client
from discord.utils import get

from main import bot
from helper.EmbedCreator import EmbedCreator
import json


@bot.event
async def on_raw_reaction_add(data):
    message_id = None
    with open('message_id.json', 'r') as file:
        message_id_dict = json.load(file)
        message_id = message_id_dict['role_message']

    print(message_id)
    if data.message_id == message_id:
        # replace this with id of the 'Hunter' role
        role_id = 857795407437758496

        if data.emoji.name == '1️⃣':
            role = get(data.member.guild.roles, id=role_id)
            try:
                await data.member.add_roles(role)
            except Exception as e:
                print(e)