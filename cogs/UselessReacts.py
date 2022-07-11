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

    @commands.command(brief="Replies to messages that contain 'sekunde', with '1'")
    async def on_message(self, ctx):
        if str(ctx.message).lower() == "sekunde":
            time.sleep(1)

            await ctx.send("1", delete_after=30)


def setup(client):
    client.add_cog(UselessReacts(client))
