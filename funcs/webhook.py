import discord
from discord.ext import commands
import aiohttp

class WebhookInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_webhooks=True)
    async def wb(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            webhooks = await ctx.guild.webhooks()
            if not webhooks:
                print("There are not any webhooks")
                return
            print(f"\n=== {len(webhooks)} webhooks on server '{ctx.guild.name}' ===")
            for webhook in webhooks:
                print(f"  Name {webhook.name}")
                print(f"  ID: {webhook.id}")
                print(f"  Channel: {webhook.channel.name if webhook.channel else 'Neznámý'}")
                print(f"  URL: {webhook.url}")
                print("-----------------------------------------")
        except discord.Forbidden:
            print("Bot doesnt have perms to see webhooks.")
        except Exception as e:
            print(f"Error: {e}")

async def setup(bot):
    await bot.add_cog(WebhookInfo(bot))