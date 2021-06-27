# This module contains all basic commands of the bot

import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import asyncio
import time
from discord import client
from discord.utils import get
import json

from main import bot
from helper.EmbedCreator import EmbedCreator
from discord.colour import Colour


# Custom help message - to be done
bot.remove_command('help')


@bot.command()
async def setup(ctx):
    try:
        # Grab id for the respective guild.
        guild = ctx.guild
        # Add halloween event category for organisation.
        event_category = await guild.create_category("Halloween Event", overwrites=None, reason=None)
        # Add info text channel under Halloween Event category.
        await guild.create_text_channel('Info', overwrites=None, category=event_category, reason=None)
        await guild.create_text_channel('Boss', overwrites=None, category=event_category, reason=None)
        await guild.create_text_channel('Hunting Ground', overwrites=None, category=event_category, reason=None)
        await guild.create_text_channel('Shop', overwrites=None, category=event_category, reason=None)
    except Exception as e:
        print(e)


@bot.command()
async def teardown(ctx):
    category_channel_list = ctx.guild.categories
    channel = ctx.channel
    await channel.send("```Are you sure you wanna delete this event? Type 'y' or 'yes'```")

    def reply_check(message):
        return message.content in ['y', 'yes'] and message.channel == channel

    try:
        await bot.wait_for('message', check=reply_check, timeout=5.0)
    except asyncio.TimeoutError:
        await channel.send("```Command to teardown has expired. Try again.```")
    else:
        try:
            for category in category_channel_list:
                if category.name == "Halloween Event":
                    for channel in category.channels:
                        await channel.delete()
                    await category.delete()
                    break
        except Exception as e:
            print(e)


@bot.command()
async def role_setup(ctx, *, channel_id=None):
    # If the target channel is unspecified, it will send the message to the current channel
    if channel_id is None:
        channel_id = ctx.channel.id
    else:
        channel_id = int(channel_id)
    
    # Fetch the target channel
    target_channel = get(ctx.guild.channels, id=channel_id)

    # Send a message and react to that message
    message = await target_channel.send('React to this message to get the Hunter role.')
    
    message_data = {'role_message': message.id}

    with open('message_id.json', 'w') as file:
        json.dump(message_data, file, indent=4)

    await message.add_reaction('1\N{variation selector-16}\N{combining enclosing keycap}')


# This command delete the role from the server (when the event ends)
@bot.command()
async def hunt_the_hunters(ctx):
    # Find the 'Hunter' role
    guild = ctx.guild
    role_to_remove = None
    for role in guild.roles:
        if 'Hunter' in role.name:
            role_to_remove = role
            break

    await role.delete()
    await ctx.send('```The Hunter role has been deleted```')


# Give a medal role to winnners
@bot.command()
async def the_winners_are(ctx):

    guild = ctx.guild
    winner_role = await guild.create_role(name='Halloween Event Winner', colour=Colour.gold())

     # Add the role members in the command to the 'winners' list
    winners = []
    for member in ctx.message.mentions:
        winners += [member]

    for player in winners:
        await player.add_roles(winner_role)


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
