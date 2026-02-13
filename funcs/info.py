# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def change_info(self,ctx):
        ICON = "assets/pfp.webp"
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.guild.edit(name="popelka was here")
        print(f"name changed to: popelka was here")
        if os.path.exists(ICON):
            with open(ICON, 'rb') as f:
                icon_bytes = f.read()
                await ctx.guild.edit(icon=icon_bytes)
                print("icon changed")
        else:
            print(f"file {ICON} doesnt exist, skipping icon change")
            pass

    @commands.command(aliases=["i", "serverinfo", "list"])
    async def info(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        guild = ctx.message.guild
        channels = guild.channels
        roles = guild.roles
        members = guild.members

        print("------- Server Info -------")
        print(f"Server Name: {guild.name}")
        print(f"Members: {len(members)}")
        print(f"Channels: {len(channels)}")
        print(f"Roles: {len(roles)}")
        print("---------------------------")

async def setup(bot):
    await bot.add_cog(Info(bot))