import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='&', intents=intents)

# Load .env file
load_dotenv()

@bot.event
async def on_ready():
    print(f"{bot.user} is up and running.")
    
@bot.command()
async def info(ctx):
    await ctx.send(f"Welcome to the Canvas Helper bot!  Here are the commands you can use: \
             \n help - prints this message \
             \n Announcements - prints the announcements for the course \
             \n Grade - prints your current grade for a course \
             \n Poll - creates a poll for a course", ephemeral=True) 
    
@bot.command()
async def upcoming(ctx):
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
async def create_poll(ctx, arg):
    emojis = [':white_check_mark:', ':x:']
    await ctx.send(arg)
    for emoji in emojis:
        await ctx.add_reaction(emoji)

bot.run(os.getenv("TOKEN"))