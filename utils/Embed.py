import discord, sys

class Embed():
    def __init__(self,client):
        self.client = client 
    
    #Below are function for the bots embedded messages
    def startPurgeMessage(self, user_name):
        title = ":warning: Purging {0}'s messages :warning:".format(user_name)
        embed = discord.Embed(title=title, description="Please refrain from sending any messages during this time. You will be alerted when the process has completed.", colour=0xc47608)
        return embed

    def endPurgeMessage(self, user_name, messages_deleted, str_runtime):
        embed = discord.Embed(title=":ballot_box_with_check: The purge has been completed :ballot_box_with_check: ", colour=0x239e2b)
        embed.add_field(name="Target user: ", value=user_name, inline=False)
        embed.add_field(name="Total Messages Deleted: ", value=messages_deleted, inline=False)
        embed.add_field(name="Total Runtime: ", value=str_runtime, inline=True)
        return embed
        
    def errMessage(self, error_str):
        embed = discord.Embed(title=error_str, colour=0xb90909)
        return embed