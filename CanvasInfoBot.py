import discord
import config
from discord.ext import commands
import canvasapi
import datetime 

TOKEN = config.tokens["discord"]
CHANNEL_ID = 1075559490289668201

bot = commands.Bot(command_prefix = "&", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Canvas Info Bot up and running!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Canvas Info Bot up and running!")

@bot.command()
async def upcoming(ctx):
    TOKEN2 = config.tokens['canvas']
    BASEURL = 'https://templeu.instructure.com/'

    canvas_api = canvasapi.Canvas(BASEURL, TOKEN2)

    user = canvas_api.get_user('self')

    print(user.name)

    softwareDesign = canvas_api.get_course(123654) 
    assignments = softwareDesign.get_assignments()

    for assignment in assignments:
        due_date = str(assignment.due_at)

        readable = due_date
        if(due_date != "None"):
            t1 = datetime.datetime(int(due_date[0:4]), int(due_date[5:7]), int(due_date[8:10]))
            t2 = datetime.datetime.now()
            if(t1>t2):
                readable_date = f"{due_date[5:10]}-{due_date[0:4]}"
                readable_time = f"{due_date[11:16]} UTC"
                print(f"{assignment} is due on {readable_date} at {readable_time}\n")
                await ctx.send(f"{assignment}\n **due on {readable_date} at {readable_time}**\n\n")
@bot.command()
async def help(ctx):
    await ctx.send("This is a placeholder help command feature!\n&upcoming: Displays upcoming assignments.")

bot.run(TOKEN)