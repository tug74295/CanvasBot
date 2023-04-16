import discord
import keys
from discord.ext import commands
import canvasapi
import datetime 
import requests

DISCORD = keys.tokens["discord"]
CANVAS = keys.tokens['canvas']
BASEURL = 'https://templeu.instructure.com/'
canvas_api = canvasapi.Canvas(BASEURL, CANVAS)

current_class = canvas_api.get_courses()[0]

bot = commands.Bot(command_prefix = "&", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Canvas Info Bot up and running!")

@bot.command()
async def course(ctx):
    await ctx.send("Your courses:\n")

    courses = canvas_api.get_courses(enrollment_state='active')

    select = 0
    for course in courses:
        name = course.name
        id = course.id
        await ctx.send(f"({select}) {name}\n")
        select += 1

    await ctx.send(f"select a course\n") 

    def check(m):
        if m.content.isdigit():
            global pick 
            pick = int(m.content)
            return range(0,select).count(pick) > 0

    msg = await bot.wait_for('message', check=check, timeout = 15)
    print(courses[pick].id)
    global current_class 
    current_class = canvas_api.get_course(courses[pick].id)
    await ctx.send(f'{courses[pick].name}\n')
    
@bot.command()
async def select(ctx):
    print("Select a course")

@bot.command()
async def upcoming(ctx):
    none_upcoming = True

    user = canvas_api.get_user('self')
    print(user.name)

    #softwareDesign = canvas_api.get_course(123654) 
    assignments = current_class.get_assignments()

    for assignment in assignments:
        due_date = str(assignment.due_at)

        readable = due_date
        if(due_date != "None"):
            t1 = datetime.datetime(int(due_date[0:4]), int(due_date[5:7]), int(due_date[8:10]))
            t2 = datetime.datetime.now()
            if(t1>t2):
                none_upcoming = False
                readable_date = f"{due_date[5:10]}-{due_date[0:4]}"
                readable_time = f"{due_date[11:16]} UTC"
                print(f"{assignment} is due on {readable_date} at {readable_time}\n")
                await ctx.send(f"{assignment}\n **due on {readable_date} at {readable_time}**\n\n")
    
    if(none_upcoming):
        await ctx.send(f"You have no upcoming assignments in {current_class.name}!")

bot.run(DISCORD)