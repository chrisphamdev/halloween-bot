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


@client.event
async def on_raw_reaction_add(data):
    message_id = None
    with open('message_id.json', 'r') as file:
        message_id_dict = json.load(file)
        message_id = message_id_dict['role_message']

    print(message_id)
    if data.message_id == message_id:
        for txt_channel in data.member.guild.channels:
            if txt_channel.name == 'info':
                host_channel = txt_channel
                break
        msg = await host_channel.fetch_message(data.message_id)

        # replace this with id of the 'Hunter' role
        role_id = 760392204710969354

        if data.emoji.name == 'crossed_swords':
            role = get(data.member.guild.roles, id=role_id)
            await data.member.add_roles(role)
