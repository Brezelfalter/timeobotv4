import os
import discord
import json
import time
import asyncio 

from discord.ext import commands


BASE_DIRECTORY = ""
PREFIX = "-4"

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
client.remove_command("help")





def lostFunc(client):
    ''' 
    importing all cogs
    for this go to 'cogs' im BASE_DIRECTORY and import all files that end with '.py'
    '''
    for filename in os.listdir(f"{os.path.abspath('.')}/cogs"):
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(e)










def main():
    # keep_alive.keep_alive()
    lostFunc(client)
    client.run(os.environ.get("TOKEN"))
    
if __name__ == "__main__":
    main()