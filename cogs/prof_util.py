import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord import SlashOption
from nextcord import Embed
from datetime import datetime

class prof_util(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Our test server id. Change in the future.
    server_id = 1075559489631170590

    @nextcord.slash_command(name='announce', description='Make an announcement on Canvas.')
    async def announcement(self, interaction : Interaction, title : str, content : str):
        pass

    @nextcord.slash_command(name='poll', description='Create a poll.', guild_ids=[server_id])
    async def create_poll(self, 
                          interaction : Interaction,
                          question : str = SlashOption(name='question'),
                          options : str = SlashOption(name='options')):
        numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

        options_list = options.split()
            
        if len(options) > 10:
            await interaction.response.send_message("You can only supply a maximum of 10 options.")
            return

        embed = Embed(title='Poll',
                      description=question,
                      color=interaction.user.color,
                      timestamp=datetime.utcnow()
                      )
        fields=[("Options", "\n".join([f'{numbers[i]} {option}' for i, option in enumerate(options_list)]), False),
                ("Instructions", "React to cast a vote.", False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await interaction.response.send_message(embed=embed)
def setup(client):
    client.add_cog(prof_util(client))