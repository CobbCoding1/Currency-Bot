import discord
import requests
import json
import random
import os

client = discord.Client()

def get_meme():
  response = requests.get('https://api.imgflip.com/get_memes')
  json_data = json.loads(response.text)
  return(json_data['data']['memes'][random.randint(0, 10)]['url'])

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  
  if(message.content.startswith('.currency')):
    await message.channel.send('You have earned +1 currency!')
  if(message.content.startswith('.currency') and message.content.endswith('meme')):
    await message.channel.send(get_meme())

client.run(os.getenv('TOKEN'))