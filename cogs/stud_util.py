import nextcord
import os
from dotenv import load_dotenv 
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions
import canvasapi

load_dotenv('../.env')
current_class = 0

class stud_util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name='upcoming', description='List the upcoming assignments.')
    async def get_upcoming(self, interaction : Interaction, course : str):
        pass

    @nextcord.slash_command(name='grades', description='View grade for a specific class.')
    async def view_grade(self, interaction : Interaction, course : str):
        pass

    @nextcord.slash_command(name='due', description='Get due date for a specific assignment.')
    async def get_due_date(self, interaction : Interaction, assignment : str):
        pass
    @nextcord.slash_command(name='courses', description='List enrolled courses.')
    async def get_courses(self, interaction : Interaction):
        await interaction.response.send_message("Here are your courses:\n")

        CANVAS = os.getenv("CANVAS")
        BASEURL = 'https://templeu.instructure.com/'
        canvas_api = canvasapi.Canvas(BASEURL, CANVAS)
        
        user = canvas_api.get_user('self')
        print(user.name)

        courses = canvas_api.get_courses(enrollment_state='active')

        select = 0
        output = ""
        for course in courses:
            name = course.name
            id = course.id
            output += f"({select}) {name}\n"
            select += 1

        output += "+ Enter a number to select the corresponding course +\n"
        await interaction.followup.send(f"```diff\n{output}```") 

        def check(m):
            if m.content.isdigit():
                global pick 
                pick = int(m.content)
                print(pick)
                return range(0,select).count(pick) > 0

        msg = await self.client.wait_for('message', check=check, timeout = 15)
        print(courses[pick].id)
        global current_class 
        current_class = canvas_api.get_course(courses[pick].id)
        await interaction.followup.send(f'Current course: **{courses[pick].name}**\n')

def setup(client):
    client.add_cog(stud_util(client))