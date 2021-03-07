from replit import db
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

def add_currency(message):
  print(str(message.author.name))

  #print(message.author.id)
  if(str(message.author.name) in db.keys()):
    value = db[str(message.author.name)]
    print("lel" + db[message.author.name])
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

  if(msg.startswith('.currency') and msg.endswith('meme')):
    await message.channel.send(get_meme())
  if(msg.startswith('.currency') and msg.endswith('inventory')):
    await message.channel.send(get_currency(message))

client.run(os.getenv('TOKEN'))