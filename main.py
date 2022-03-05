# main.py
import os
import discord as ds
from dotenv import load_dotenv

import bookClub as bc

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = ds.Intents.all()
client = ds.Client(intents=intents)

client = bc.BCClient()
client.run(TOKEN)
