import discord
from discord import app_commands
from discord.ext import commands as cmd

class other_util(cmd.Cog):
    def __init__(self, client):
        self.client = client
    
    @app_commands.command(name='help', description='List command names and descriptions.')
    async def help(self, interaction=discord.Interaction):
        await interaction.response.send_message(f"Welcome to the Canvas Helper bot!  Here are the commands you can use: \
             \n help - prints this message \
             \n Announcements - prints the announcements for the course \
             \n Grade - prints your current grade for a course \
             \n Poll - creates a poll for a course", ephemeral=True)

    @app_commands.command(name='login', description='Login to Canvas.')
    async def login(self, interaction=discord.Interaction):
        pass

async def setup(client):
    await client.add_cog(other_util(client))