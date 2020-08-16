import discord, sys
from datetime import datetime
from discord.ext import commands

class PurgeBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    async def purge(self, ctx):
        counter = 0
        async for message in ctx.message.channel.history():
            if str(message.author) == "smelkaaa#0283":
                counter += 1
                isDeleted = False
                while not isDeleted:
                    try:
                        await message.delete(delay=None)
                        isDeleted = True
                    except:
                        next
        print(counter)
   
    @commands.command()
    async def kill(self, ctx):
        if str(ctx.message.author) == "smelkaaa#0283":
            await ctx.bot.logout()
        else:
            await ctx.send("You have no power here {0} :^)".format(ctx.message.author.mention))

def setup(client):
    client.add_cog(PurgeBot(client))