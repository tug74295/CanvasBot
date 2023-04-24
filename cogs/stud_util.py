import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions
import canvasapi

class stud_util(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Our test server id. Change in the future.
    server_id = 1075559489631170590

    @nextcord.slash_command(name='upcoming', description='List the upcoming assignments.')
    async def get_upcoming(self, interaction : Interaction, course : str):
        pass

    @nextcord.slash_command(name='grades', description='View grade for a specific class.')
    async def view_grade(self, interaction : Interaction):
        pass

    @nextcord.slash_command(name='due', description='Get due date for a specific assignment.')
    async def get_due_date(self, interaction : Interaction, assignment : str):
        pass

    @nextcord.slash_command(name='courses', description='List enrolled courses.')
    async def get_courses(self, interaction : Interaction) -> canvasapi.course.Course:
        await interaction.response.send_message("Here are your courses:\n")

        courses = canvasapi.get_courses(enrollment_state='active')

        select = 0
        for course in courses:
            name = course.name
            id = course.id
            await interaction.response.send_message(f"({select}) {name}\n")
            select += 1

        await interaction.response.send_message(f"Enter a number to select the corresponding course\n")

        def check(message : nextcord.message):
            if message.content.isdigit():
                global pick 
                pick = int(message.content)
                return range(0,select).count(pick) > 0
            
        await self.client.wait_for('message', check=check, timeout = 15)
        print(courses[pick].id)
        global current_class 
        current_class = canvasapi.get_course(courses[pick].id)
        await interaction.response.send_message(f'Current course: **{courses[pick].name}**\n')
        self.curr_course = courses[pick]


def setup(client):
    client.add_cog(stud_util(client))