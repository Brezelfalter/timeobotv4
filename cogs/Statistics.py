import discord
import json
import asyncio
import time

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands, tasks
from datetime import timedelta, date, datetime
from discord_components import DiscordComponents, ComponentsBot, Button



# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    OWNERID = data["bot_info"]["owner-id"]




class Statistics(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        cur_timestamp = int(time.time())
        cur_date = str(date.today().strftime("%d/%m/%Y")).replace("/", ".")
        
        guild_id = after.guild.id
        
        
        print("update")

        if str(before.status) == str(after.status):
            return
            
        data = self.json_read(f"{BASE_DIRECTORY}data/statistics/timestamps.json")
        
        data_status = data[str(after.id)]["status"]
        data_timestamp = int(data[str(after.id)]["timestamp"])
        time_difference = cur_timestamp - data_timestamp


        
        with open(f"{BASE_DIRECTORY}data/statistics/timestamps.json") as file:
            data = json.load(file)
        
            del data["jafs"][to_remove]
        
            with open(r"Tests\json_tests\test.json", "w") as file:
                json.dump(data, file, indent=4)
        
        

        
        
    def update_total_time(self, guild_id, date):#
        data = self.json_read(f"{BASE_DIRECTORY}data/statistics/total_time.json")
            
        try:
            date = data[f"{guild_id}"][f"{date}"]
        except:
            with open(r"Tests\json_tests\test.json", "r+") as file:
                data = json.load(file)
                dictionary = {
                    f"{date}": {
                        "total_online": 0,
                        "total_idle": 0,
                        "total_dnd": 0,
                        "total_offline": 0
                    }
                }

                data[f"{guild_id}"].update(str(dictionary))
                file.seek(0)
                json.dump(data, file, indent=4)


        save_online = data[f"{guild_id}"][f"{date}"]["total_online"]
        save_idle = data[f"{guild_id}"][f"{date}"]["total_idle"]
        save_dnd = data[f"{guild_id}"][f"{date}"]["total_dnd"]
        save_offline = data[f"{guild_id}"][f"{date}"]["total_offline"]
        

            
        
    def json_read(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return data

    def json_update(filename, push_data, keys=None):
        # keys as list in order
        # push_data as dict

        with open(filename, "r+") as file:
            data = json.load(file)
            
            if keys != None:
                for item in keys: 
                    data = data[f"{keys[keys.index(item)]}"]

            data.update(push_data)
            file.seek(0)
            json.dump(data, file, indent=4)

    def json_remove(filename, remove_data, keys=None):
        # keys as list in order
        # remove data = value as string

        with open(filename) as file:
            data = json.load(file)

            if keys != None:
                for item in keys: 
                    data = data[f"{keys[keys.index(item)]}"]

            del data[remove_data]

            with open(r"Tests\json_tests\test.json", "w") as file:
                json.dump(data, file, indent=4)
                
            
            
        
# print(f"[2] User: [{after.name}]\nBefore: [{before.status}]\nAfter: [{after.status}]\n\n")

        





def setup(client):
    client.add_cog(Statistics(client))