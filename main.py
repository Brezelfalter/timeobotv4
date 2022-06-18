from logging import exception
import os, sys
# import keep_alive
import discord
import json
import time
import asyncio 

from discord.ext import commands


BASE_DIRECTORY = ""
PREFIX = "-4"

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
client.remove_command("help")





async def lostFunc(client):
    ''' 
    importing all cogs
    for this go to 'cogs' im BASE_DIRECTORY and import all files that end with '.py'
    '''
    for filename in os.listdir(f"{os.path.abspath('.')}/cogs"):
        if filename.endswith(".py"):
            try:
                await client.load_extension(f"cogs.{filename[:-3]}")
            except exception as e:
                print(e)






print(os.path.abspath("main.py"), file=sys.stderr)








def main():
    # keep_alive.keep_alive()
    asyncio.run(lostFunc(client))
    client.run(os.environ.get("TOKEN"))
    
if __name__ == "__main__":
    main()
