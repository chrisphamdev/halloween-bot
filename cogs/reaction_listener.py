# This module handles any reaction_add event
from discord.ext import commands
from discord.utils import get


class ReactionListenerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Reaction listener cog has been initialised.')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        message_id = self.bot.config_helper.role_message_id

        if data.message_id == message_id:
            # replace this with id of the 'Hunter' role
            role_id = self.bot.config_helper.role_id

            if data.emoji.name == '1️⃣':
                role = get(data.member.guild.roles, id=role_id)
                try:
                    await data.member.add_roles(role)
                except Exception as e:
                    print(e)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        message_id = self.bot.config_helper.role_message_id

        if data.message_id == message_id:
            role_id = self.bot.config_helper.role_id

            if data.emoji.name == '1️⃣':
                guild = self.bot.get_guild(data.guild_id)
                role = get(guild.roles, id=role_id)
                member = guild.get_member(data.user_id)
                try:
                    await member.remove_roles(role)
                except Exception as e:
                    print(e)


def setup(bot):
    bot.add_cog(ReactionListenerCog(bot))
