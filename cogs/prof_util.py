import discord
from discord.ext import commands as cmd

class utilities(cmd.Cog):
    def __init__(self, client):
        self.client = client

    @cmd.command()
    def announcement(self, ctx, arg):
        pass

    @cmd.command()
    def create_poll(self, ctx, arg):
        pass
