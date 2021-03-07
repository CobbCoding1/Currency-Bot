from replit import db
from keep_alive import keep_alive
import discord
import requests
import json
import random
import os

#I need to add comments in this file.

client = discord.Client()

def get_meme():
  response = requests.get('https://meme-api.herokuapp.com/gimme/wholesomememes')
  json_data = json.loads(response.text)
  return(json_data['url'][0])

def add_currency(message):
  print(str(message.author.name))

  if(str(message.author.name) in db.keys()):
    value = db[str(message.author.name)]
    print(db[message.author.name])
    db[str(message.author.name)] = str(int(value) + 10)
    print(12345)
  else:
    db[str(message.author.name)] = str(message.author.name)
    db[message.author.name] = str(10)
    print(54321)

  print(db[str(message.author.name)])

def get_currency(message):
  return("You currently have: " + db[str(message.author.name)])
  

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if(message.author == client.user):
    return

  msg = message.content
  
  add_currency(message)
  await message.channel.send('You have earned +10 currency! -THIS IS A DEBUG MESSAGE, WILL REMOVE LATER')

  if(msg.startswith('.cur') and msg.endswith('meme')):
    await message.channel.send(get_meme())
  if(msg.startswith('.cur') and msg.endswith('inventory')):
    await message.channel.send(get_currency(message))

keep_alive()
client.run(os.getenv('TOKEN'))