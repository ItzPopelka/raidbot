# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def change_info(self,ctx):
        ICON = "pfp.webp"
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.guild.edit(name="popelka was here")
        print(f"nazev zmenen na: popelka was here")
        if os.path.exists(ICON):
            with open(ICON, 'rb') as f:
                icon_bytes = f.read()
                await ctx.guild.edit(icon=icon_bytes)
                print("ikonka zmenena")
        else:
            print(f"soubor {ICON} neexistuje")

    @commands.command()
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