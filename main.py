from replit import db
import discord
import requests
import json
import random
import os

#test

client = discord.Client()

def get_meme():
  response = requests.get('https://api.imgflip.com/get_memes')
  json_data = json.loads(response.text)
  return(json_data['data']['memes'][random.randint(0, 10)]['url'])

def add_currency(message):
  print(message.author.id)
  print(db[str(message.author.id)])
  db[str(message.author.id)] = str(int(db[str(message.author.id)]) + 10)

  print(db[str(message.author.id)])

def get_currency(message):
  return("You currently have: " + db[str(message.author.id)])
  

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if(message.author == client.user):
    return

  msg = message.content
  
  add_currency(message)
  await message.channel.send('You have earned +10 currency!')

  if(msg.startswith('.currency') and msg.endswith('meme')):
    await message.channel.send(get_meme())
  if(msg.startswith('.currency') and msg.endswith('inventory')):
    await message.channel.send(get_currency(message))

client.run(os.getenv('TOKEN'))