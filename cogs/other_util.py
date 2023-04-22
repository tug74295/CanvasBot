import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions


class other_util(commands.Cog):
    def __init__(self, client):
        self.client = client

    server_id = 1075559489631170590
    
    @nextcord.slash_command(name='help', description='List command names and descriptions.', guild_ids=[server_id])
    async def help(self, interaction : Interaction):
        await interaction.response.send_message(f"Welcome to the Canvas Helper bot!  Here are the commands you can use: \
             \n help - prints this message \
             \n Announcements - prints the announcements for the course \
             \n Grade - prints your current grade for a course \
             \n Poll - creates a poll for a course", ephemeral=True)

    @nextcord.slash_command(name='login', description='Login to Canvas.', guild_ids=[server_id])
    async def login(self, interaction : Interaction):
        pass

def setup(client):
    client.add_cog(other_util(client))