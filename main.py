import discord
import os
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


















def main():
    keep_alive.keep_alive()
    time.sleep(1)
    client.run(input("token: "))
    
if __name__ == "__main__":
    main()
