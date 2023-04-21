import discord
from discord import app_commands
from discord.ext import commands as cmd

class stud_util(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='upcoming', description='List the upcoming assignments.')
    async def get_upcoming(self, interaction : discord.Interaction, course : str):
        pass

    @app_commands.command(name='grades', description='View grade for a specific class.')
    async def view_grade(self, interaction : discord.Interaction, course : str):
        pass

    @app_commands.command(name='due', description='Get due date for a specific assignment.')
    async def get_due_date(self, interaction : discord.Interaction, assignment : str):
        pass

async def setup(client):
    await client.add_cog(stud_util(client))