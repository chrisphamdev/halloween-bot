"""
    This file is for all the admin commands to setup and to remove the event from the server.
"""

import discord
import asyncio

from discord.ext import commands
from discord.utils import get

from helper.EmbedCreator import EmbedCreator
from discord.colour import Colour


class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # TODO implement custom help command.
        # self.bot.remove_command('help')
        print('AdminCog has been initialised.')

    # Unlike the bot object, a cog must iterate through a list of commands to retrieve it.
    def find_command(self, name: str) -> discord.ext.commands.Command:
        for command in self.walk_commands():
            if command.name == name:
                return command

    @commands.command()
    async def event_start(self, ctx: discord.ext.commands.Context):

        # Create categories and setup.
        setup_command = self.find_command('setup')
        await ctx.send("```Creating channels for the event...```")
        await setup_command.invoke(ctx)

        # Create roles and role assignment message.
        setup_role_command = self.find_command('role_setup')
        await ctx.send("```Creating roles for the event...```")
        await setup_role_command.invoke(ctx)

    @commands.command()
    async def event_stop(self, ctx: discord.ext.commands.Context):

        # Removes previously created channels and category.
        tear_down_command = self.find_command('teardown')
        await ctx.send('```Finding and deleting category and its respective text channels...```')
        await tear_down_command.invoke(ctx)

        # Remove previously created role created for the event.
        await ctx.send('```Finding and deleting role...```')
        remove_role_command = self.find_command('hunt_the_hunters')
        await remove_role_command.invoke(ctx)

    @commands.command()
    async def setup(self, ctx: discord.ext.commands.Context):
        if ctx.invoked_subcommand is AdminCog.event_start:
            await ctx.send('Chaining setup co-routine.')
        try:
            config_helper = self.bot.config_helper
            # Grab id for the respective guild.
            guild = ctx.guild

            # Add halloween event category for organisation.
            event_category = await guild.create_category(
                'Halloween Event',
                overwrites=None,
                reason='Setting up text channel category for Halloween Event 2021'
            )
            config_helper.category_id = event_category.id
            # Add info text channel under Halloween Event category.
            info_channel = await guild.create_text_channel(
                'Info',
                overwrites=None,
                category=event_category,
                reason='Setting up text channel for Halloween Event 2021'
            )
            config_helper.info_channel_id = info_channel.id

            boss_channel = await guild.create_text_channel(
                'Boss',
                overwrites=None,
                category=event_category,
                reason='Setting up text channel for Halloween Event 2021'
            )
            config_helper.boss_channel_id = boss_channel.id

            hunting_channel = await guild.create_text_channel(
                'Hunting Ground',
                overwrites=None,
                category=event_category,
                reason='Setting up text channel for Halloween Event 2021'
            )
            config_helper.hunting_channel_id = hunting_channel.id

            shop_channel = await guild.create_text_channel(
                'Shop',
                overwrites=None,
                category=event_category,
                reason='Setting up text channel for Halloween Event 2021'
            )
            config_helper.shop_channel_id = shop_channel.id

        except Exception as e:
            print(e)

    @commands.command()
    async def teardown(self, ctx):
        await ctx.channel.send("```Are you sure you wanna delete this event? Type 'y' or 'yes'```")

        def reply_check(message):
            return message.content in ['y', 'yes'] and message.channel == ctx.channel

        try:
            await self.bot.wait_for('message', check=reply_check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.channel.send("```Command to teardown has expired. Try again.```")
        else:
            try:
                info_channel = ctx.guild.get_channel(self.bot.config_helper.info_channel_id)
                boss_channel = ctx.guild.get_channel(self.bot.config_helper.boss_channel_id)
                hunting_channel = ctx.guild.get_channel(self.bot.config_helper.hunting_channel_id)
                shop_channel = ctx.guild.get_channel(self.bot.config_helper.shop_channel_id)
                category = get(ctx.guild.categories, id=self.bot.config_helper.category_id)

                await info_channel.delete()
                del self.bot.config_helper.info_channel_id
                await boss_channel.delete()
                del self.bot.config_helper.boss_channel_id
                await hunting_channel.delete()
                del self.bot.config_helper.hunting_channel_id
                await shop_channel.delete()
                del self.bot.config_helper.shop_channel_id
                await category.delete()
                del self.bot.config_helper.category_id

            except Exception as e:
                print(e)

    @commands.command()
    async def role_setup(self, ctx):

        role = None
        try:
            # Create role and save it to file.
            role = await ctx.guild.create_role(
                name='Hunter',
                # Appears in the audit log.
                reason='Add Hunter role for the Halloween Event.',
                colour=Colour.gold()
            )

            self.bot.config_helper.role_id = role.id

        except discord.HTTPException:
            await ctx.send('```Connection Issue: Cannot create Hunter role, try again.```')

        if role:
            # If the target channel is unspecified, it will send the message to the current channel
            channel_id = self.bot.config_helper.info_channel_id
            if channel_id is None:
                channel_id = ctx.channel.id
            else:
                channel_id = int(channel_id)

            # Fetch the target channel
            target_channel = get(ctx.guild.channels, id=channel_id)
            # Send a message and react to that message
            message = await target_channel.send('```React to this message to get the Hunter role.```')
            # Register the role message id with the config helper
            self.bot.config_helper.role_message_id = message.id
            await message.add_reaction('1\N{variation selector-16}\N{combining enclosing keycap}')

    # This command delete the role from the server (when the event ends)
    @commands.command()
    async def hunt_the_hunters(self, ctx):
        # Find the 'Hunter' role
        role_name = "Hunter"
        guild = ctx.guild
        role_to_remove = None

        role_id = self.bot.config_helper.role_id

        if role_id:
            role_to_remove = get(guild.roles, id=role_id)
        else:
            # Finds the role object to be removed from the guild.
            for role in guild.roles:
                if role.name == role_name:
                    role_to_remove = role
                    break

        try:
            await role_to_remove.delete()
            del self.bot.config_helper.role_id
            # TODO the message is deleted via text channel deletion. No need to store and delete this manually.
            del self.bot.config_helper.role_message_id
        except discord.HTTPException:
            await ctx.send(f'```Connection issue: Failed to delete {role_name}, try again.```')

    # Give a medal role to winners
    @commands.command()
    async def reward_winners(self, ctx):

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

    @commands.command()
    async def print_id(self, ctx):
        await ctx.send(f'```{self.bot.config_helper}```')

    # # Replace default help command to this one.
    # @bot.command()
    # async def help(ctx):
    #     await ctx.send('The rule-set can be accessed here.')
    #     # TO BE ADDED: GAME RULE

    # bot info
    @commands.command()
    async def info(self, ctx):
        info_str = 'This bot was created by Wesley Heath and Chris Pham for the UoA Esports server. Any feedback will '\
                'be appreciated. '
        embed = EmbedCreator('Halloween Bot', 'Information', info_str, 'Powered by UoA Esports.')
        await ctx.send(embed=embed.get_embed())

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! This message took {round(self.bot.latency * 1000)}ms to respond.')


def setup(bot):
    bot.add_cog(AdminCog(bot))
