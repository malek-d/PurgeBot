import discord, sys
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure, BadArgument
from datetime import datetime
from discord.ext import commands
from utils.Embed import Embed

class PurgeBot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.embed = Embed(client)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx):
        #Checks to see if a user has been mentioned if not asks user to input a valid user - e.g. $purge @<user>
        try:
            user_name = ctx.message.mentions[0].name
            user = str(ctx.message.mentions[0].id)

            await ctx.send(embed=self.embed.startPurgeMessage(user_name))
        except:
            await ctx.send(embed=self.embed.errMessage("You have not mentioned a valid user. Please mention a valid user after the purge command."))
            return
        
        #Loops through messages within channel and deletes any that are posted from selected user
        messages_deleted = 0
        start_time = datetime.now()
        async for message in ctx.message.channel.history(limit=None):
            if str(message.author.id) == user:
                isDeleted = False
                while not isDeleted:
                    try:
                        await message.delete(delay=None)
                        messages_deleted += 1
                        isDeleted = True
                    except:
                        next

        #Calculates the total runtime in minutes & seconds          
        end_time = datetime.now()
        runtime = divmod((end_time - start_time).seconds, 60)
        str_runtime = str(runtime[0]) + " minutes and " + str(runtime[1]) + " seconds"

        #print(messages_deleted)
        await ctx.send(embed=self.embed.endPurgeMessage(user_name,messages_deleted,str_runtime))

    # Enable the below for testing
    @commands.command()
    @has_permissions(manage_messages=True)
    async def pollute(self, ctx):
        count = 0
        while count != 200:
            await ctx.send("test " + str(count))
            count += 1

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(embed=self.embed.errMessage(":exclamation: You have no power here {0} :^) :exclamation:".format(str(ctx.message.author.name))))
        elif isinstance(error, CheckFailure):
            await ctx.send(embed=self.embed.errMessage(":exclamation: You have no power here {0} :^) :exclamation:".format(str(ctx.message.author.name))))
        elif isinstance(error, BadArgument):
            await ctx.send(embed=self.embed.errMessage(":grey_question: Could not identify target :grey_question: "))
        else:
            raise error
   
    @commands.command()
    @has_permissions(manage_messages=True)
    async def kill(self, ctx):
        await ctx.bot.logout()

def setup(client):
    client.add_cog(PurgeBot(client))