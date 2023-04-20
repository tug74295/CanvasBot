import discord
from dotenv import load_dotenv
import os

load_dotenv()

def run_bot():
    print(discord.__version__)
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said {user_message} in ({channel}).')
    
    client.run(os.getenv('TOKEN'))
