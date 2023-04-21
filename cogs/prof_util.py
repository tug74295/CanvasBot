import discord
from discord import app_commands
from discord.ext import commands as cmd

class prof_util(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='announce', description='Make an announcement on Canvas.')
    async def announcement(self, interaction, title : str, content : str):
        pass

    @app_commands.command(name='poll', description='Create a poll.')
    async def create_poll(self, interaction : discord.Interaction, title : str, content : str):
        pass

async def setup(client):
    await client.add_cog(prof_util(client))