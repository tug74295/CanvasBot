import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions

class prof_util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name='announce', description='Make an announcement on Canvas.')
    async def announcement(self, interaction : Interaction, title : str, content : str):
        pass

    @nextcord.slash_command(name='poll', description='Create a poll.')
    async def create_poll(self, interaction : Interaction, title : str, content : str):
        pass

def setup(client):
    client.add_cog(prof_util(client))