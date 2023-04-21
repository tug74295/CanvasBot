import discord
from discord import app_commands
from discord.ext import commands as cmd

class discussions(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='discuss', description='Post a discussion to Canvas.')
    async def post_dsn(self, interaction=discord.Interaction):
        pass

    @app_commands.command(name='reply', description='Reply to a discussion post.')
    async def reply(self, interaction=discord.Interaction):
        pass

async def setup(client):
    await client.add_cog(discussions(client))