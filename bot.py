# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == "!laugh":
		response = "😂😂"
		await message.channel.send(response)

	if message.content == "!biglaugh":
		response = "😂😂😂"
		await message.channel.send(response)

	if message.content == "!sad":
		response = "😐"
		await message.channel.send(response)

	if message.content == "!classic":
		response = "yea yea"
		await message.channel.send(response)		

client.run(TOKEN)