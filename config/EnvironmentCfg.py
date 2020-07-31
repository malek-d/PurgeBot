import os
from dotenv import load_dotenv

def getDiscordToken():
    load_dotenv()
    return os.getenv('DISCORD_TOKEN')