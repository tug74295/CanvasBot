from dotenv import load_dotenv 
import asyncio


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='&', intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is up and running.")
    
@client.event
async def on_load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await client.load_extension(f'cogs.{file[:-3]}')

async def main():
    await on_load()
    await client.start(os.getenv("TOKEN"))

asyncio.run(main())
