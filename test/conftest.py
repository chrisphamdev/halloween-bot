import discord
import pytest
import discord.ext.test as dpytest
from discord.ext import commands


@pytest.fixture
def bot(event_loop):
    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix=';', intents=intents, loop=event_loop)
    bot.load_extension('cogs.admin_commands')
    bot.load_extension('cogs.reaction_listener')
    dpytest.configure(bot)
    return bot


# def pytest_session_finish():
#     # Write logic to clean up after tests.
#     pass
