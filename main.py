import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  
  if(message.content.startswith('.currency')):
    await message.channel.send('You have earned +1 currency!')

client.run(os.getenv('TOKEN'))