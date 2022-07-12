import discord
import json
import asyncio
import time

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands, tasks
from datetime import datetime
from datetime import timedelta



# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    OWNERID = data["bot_info"]["owner-id"]




class UselessReacts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        print("message_event: UselessReacts.py")
        print(message)
        msg = str(message).lower()
        print(msg)

        if msg == "sekunde":
            print("HERE")
            time.sleep(1)
            print("triggered if statement: UselessReacts.py")

            await message.channel.send("1", delete_after=30)


def setup(client):
    client.add_cog(UselessReacts(client))
