# main.py
import os

import discord as ds
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = ds.Intents.all()
client = ds.Client(intents=intents)


class GenericClient(ds.Client):
    async def on_ready(self): # Notify when connected to server
        print(f'{client.user} has connected to Discord!\n')

    async def on_message(self, message):
        if message.author == client.user: # No reason to read my own messages
            return

        if message.content == '!helpme' or message.content == '!h':
            response = self.help_msg(self)

        await message.channel.send(response)

    def help_msg(self):
        return "There is no defined help for this bot at the moment"


client = GenericClient()
client.run(TOKEN)
