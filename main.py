import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv


intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='c!', intents=intents)

# Load .env file
load_dotenv()

@client.event
async def on_ready():
    print(f"{client.user} is up and running.")
    

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')
        print(f'Loaded {file}...')

client.run(os.getenv('TOKEN'))
