import os, sys

os.environ["PORT"] = "80"

import keep_alive
import discord
import json
import time

from discord.ext import commands


BASE_DIRECTORY = ""
PREFIX = "-4"

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
client.remove_command("help")




''' 
importing all cogs
for this go to 'cogs' im BASE_DIRECTORY and import all files that end with '.py'
'''
for filename in os.listdir(f"{BASE_DIRECTORY}cogs"):
    if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")







print(os.environ["PORT"], file=sys.stderr)








def main():
    keep_alive.keep_alive()
    client.run(os.environ.get("TOKEN"))
    
if __name__ == "__main__":
    main()
