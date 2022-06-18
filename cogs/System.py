from pydoc import describe
import discord
import json

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands

# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    COMMAND_BLACKLIST = data["bot_info"]["command_blacklist"]


class System(commands.Cog):
    """
    the basic system functions
    currently consisting of:
    on_ready, help, ping, load, unload 
    """
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name=f"with time (v{BOT_VERSION})"), status=discord.Status.online)

        print("Started the Bot")

    @commands.command(brief="Sends genral or specific command help. Give the argument after the command")
    async def help(self, ctx, extension=None):
        """
        Gives help, while listing all the classes that contain commands as well as
        their commands in an Embed. 
        Also states the current Bot version and advice on more specific information 
        for each command.
        """
        # deletes the message that triggered the command to keep the chat clean
        await ctx.channel.purge(limit=1)

        # declares the base for the Embed
        help_Embed = discord.Embed(
            title="Bot help**                                               **",
            description="** **",
            colour=discord.Colour.blue()
        )
        # if extension was given, give command specifiic help
        if extension:
            # get command brief
            command_brief = self.client.get_command(extension).brief

            # if command brief is not existent
            if command_brief is None:
                # set command brief to a spare value  
                command_brief = "This command does not exist, please give a valid command."

            # add a field to the Embed, which contains the command brief
            help_Embed.add_field(
                name=f"Command info:",
                value=command_brief,
                inline=False
                )
        else:
            # if programm was not ended before, send standart help
            for item in self.client.cogs:
                commands_list = []
                edited_commands = ""

                # gets all commands of one class and gets their names
                commands = self.client.get_cog(f"{item}").get_commands()
                commands = [c.name for c in commands]

                # puts all commands in a list that gets sorted alphabetically
                for command in commands:
                    commands_list.append(command)
                commands_list.sort()

                # puts all commands in a string and below each other
                for command in commands_list:
                    edited_commands = f"{edited_commands}\n{command}"
                
                #checks if there are commands and skips the editing of the embed if none exist
                if edited_commands == "":
                    continue
                
                # adds two fields to the Embed, one with the info and a second one to act as a placeholder
                help_Embed.add_field(
                    name=f"{item}:",
                    value=edited_commands,
                    inline=False
                )
                help_Embed.add_field(
                    name="** **",
                    value="** **",
                    inline=False
                )
            # adding a field with relation to individual extension information
            help_Embed.add_field(
                name = "** **",
                value = f"For more information on each command, \nuse `{PREFIX}help <command name>`  instead."
            )
        # sets the footer with the version info
        help_Embed.set_footer(
            text=f"Bot is running: v{BOT_VERSION}"
        )
        #sends the Embed and deletes it after 15s
        await ctx.send(embed=help_Embed, delete_after=15)

    @commands.command()
    async def ping(self, ctx):
        """
        returns the latency the client currently has in ms
        """
        # deletes the message that triggered the command to keep the chat clean
        await ctx.channel.purge(limit=1)

        # sends a message with the latency the client has in ms
        await ctx.send(embed=create_embed("[ping]", 'pong ({0}'.format(round(self.client.latency * 1000)) + "ms)", discord.Color.blue()), delete_after=5)

    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, extension):
        """
        loads an extension that is not active currently
        """
        # deletes the message that triggered the command to keep the chat clean
        await ctx.channel.purge(limit=1)

        # loads the extension given by the user
        self.client.load_extension(f"cogs.{extension}")

        # sends confirmation about the activation of the extension to the user
        await ctx.send(embed=create_embed("[loaded]", f"`<{extension}>` has been loaded", discord.Color.blue()), delete_after=10)

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, extension):
        """
        unloads an extension that is not active currently
        """
        # deletes the message that triggered the command to keep the chat clean
        await ctx.channel.purge(limit=1)

        if extension in COMMAND_BLACKLIST:
            blacklist_embed = discord.Embed(
                title = "[blacklisted]",
                description = f"You are not permitted to disable `<{extension}>`",
                color = discord.Color.red()
            )
            await ctx.send(embed=blacklist_embed, delete_after=10)
            return

        # unloads the extension given by the user
        self.client.unload_extension(f"cogs.{extension}")

        # sends confirmation about the deactivation of the extension to the user
        await ctx.send(embed=create_embed("[unloaded]", f"`<{extension}>` has been unloaded", discord.Color.dark_blue()), delete_after=10)


def create_embed(title, description, color):
    # create basic discord Embed with given title, discription and color
    # color format: discord.Color.blue()
    embed = discord.Embed(title = title, description = description, color = color)
    # return the embed
    return embed


async def setup(client):
    await client.add_cog(System(client))