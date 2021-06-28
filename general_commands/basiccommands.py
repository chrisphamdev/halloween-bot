# This module contains all basic commands of the bot

# import discord
# from discord.ext.commands import Bot
# from discord.ext import commands, tasks
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
async def role_setup(ctx, channel_id=None):

    role = None
    try:
        # Create role and save it to file.
        role = await ctx.guild.create_role(
            name='Hunter',
            # Appears in the audit log.
            reason='Add Hunter role for the Halloween Event.',
            colour=Colour.gold()
        )
    except discord.HTTPException:
        await ctx.send('```Connection Issue: Cannot create Hunter role, try again.```')

    if role:
        # If the target channel is unspecified, it will send the message to the current channel
        if channel_id is None:
            channel_id = ctx.channel.id
        else:
            channel_id = int(channel_id)

        # Fetch the target channel
        target_channel = get(ctx.guild.channels, id=channel_id)

        # Send a message and react to that message
        message = await target_channel.send('React to this message to get the Hunter role.')
        # Create dictionary to save data to config json file.
        message_data = {'role_message': message.id, 'role_id': role.id}

        with open('config.json', 'w+') as file:
            json.dump(message_data, file, indent=4)

        await message.add_reaction('1\N{variation selector-16}\N{combining enclosing keycap}')


# This command delete the role from the server (when the event ends)
@bot.command()
async def hunt_the_hunters(ctx):
    # Find the 'Hunter' role
    role_name = "Hunter"
    guild = ctx.guild
    role_to_remove = None

    with open('config.json', 'r') as file:
        config = json.load(file)
        try:
            role_id = config['role_id']
        except KeyError:
            await ctx.send('```Cannot find role_id in configs, will search role manually...```')

    if role_id:
        role_to_remove = get(ctx.member.guild.roles, id=role_id)
    else:
        # Finds the role object to be removed from the guild.
        for role in guild.roles:
            if role.name == role_name:
                role_to_remove = role
                break

    try:
        await role_to_remove.delete()
        await ctx.send('```The Hunter role has been deleted.```')
    except discord.HTTPException:
        await ctx.send(f'```Connection issue: Failed to delete {role_name}, try again.```')


# Give a medal role to winners
@bot.command()
async def reward_winners(ctx):

    winner_role = None
    guild = ctx.guild
    try:
        winner_role = await guild.create_role(name='Halloween Event Winner 2021', colour=Colour.gold())
    except discord.HTTPException:
        await ctx.send(f'```Connection issue: failed to create role, try Again.```')
    # Check to see if winner_role is not None.
    if winner_role:
        # Add the role members in the command to the 'winners' list
        for member in ctx.message.mentions:
            try:
                await member.add_roles(winner_role)
            except discord.HTTPException:
                await ctx.send(f'```Connection issue: Failed to add roles to {member}, try again.```')


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
