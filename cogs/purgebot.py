import discord, sys
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure, BadArgument
from datetime import datetime
from discord.ext import commands

class PurgeBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx):
        #Checks to see if a user has been mentioned if not asks user to input a valid user - e.g. $purge @<user>
        try:
            user = str(ctx.message.mentions[0].id)
        except:
            await ctx.send("You have not mentioned a valid user. Please mention a valid user after the purge command.")
            return
        
        #Loops through messages within channel and deletes any that are posted from selected user
        counter = 0
        async for message in ctx.message.channel.history():
            if str(message.author.id) == user:
                counter += 1
                isDeleted = False
                while not isDeleted:
                    try:
                        await message.delete(delay=None)
                        isDeleted = True
                    except:
                        next
        print(counter)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        elif isinstance(error, CheckFailure):
            await ctx.send("You don't have permission to do that!")
        elif isinstance(error, BadArgument):
            await ctx.send("Could not identify target")
        else:
            raise error
   
    @commands.command()
    async def kill(self, ctx):
        if str(ctx.message.author) == "smelkaaa#0283":
            await ctx.bot.logout()
        else:
            await ctx.send("You have no power here {0} :^)".format(ctx.message.author.mention))

def setup(client):
    client.add_cog(PurgeBot(client))