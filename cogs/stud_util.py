import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions
import canvasapi
import json

class stud_util(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Our test server id. Change in the future.
    server_id = 1075559489631170590

    def get_user_canvas(self, member : nextcord.User | nextcord.Member,
                        filename = 'users.json') -> str:
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            for user in file_data['users']:
                print(user['snowflake'])
                if user['snowflake'] == member.id:
                    return user['apikey']
            return "Please login using the /login command!"

    @nextcord.slash_command(name='courses', description='List enrolled courses.')
    async def get_courses(self, interaction : Interaction):
        
        API_URL = 'https://templeu.instructure.com/'
        api_key = self.get_user_canvas(member=interaction.user)

        if api_key == 'Please login using the /login command!':
            await interaction.response.send_message(api_key)
            return
        
        user = canvasapi.Canvas(API_URL, api_key)
        courses = user.get_courses(enrollment_state='active')

        await interaction.response.send_message("Here are your courses:\n")

        select = 0
        output = ""
        for course in courses:
            name = course.name
            id = course.id
            output += f"({select}) {name}\n"
            select += 1

        output += "+ Enter a number to select the corresponding course +\n"
        await interaction.followup.send(f"```diff\n{output}```") 

        def check(message : nextcord.message):
            if message.content.isdigit():
                global pick 
                pick = int(message.content)
                return range(0,select).count(pick) > 0
            
        await self.client.wait_for('message', check=check, timeout = 15)
        print(courses[pick].id)
        global current_class 

        current_class = user.get_course(courses[pick].id)
        await interaction.followup.send(f'Current course: **{courses[pick].name}**\n')


def setup(client):
    client.add_cog(stud_util(client))