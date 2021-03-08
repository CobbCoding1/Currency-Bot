from replit import db
from keep_alive import keep_alive
import discord
import requests
import json
import random
import os

# Initialize client object
client = discord.Client()

monsters = ['Bigfoot', 'Chtululu', 'Godzilla']
treasure = ['Gold', 'Diamond', 'Old Boot', 'Nothing', 'Iron']

# Get a meme from r/cleanmemes
def get_meme():
  response = requests.get('https://meme-api.herokuapp.com/gimme/cleanmemes')
  json_data = json.loads(response.text)
  return(json_data['url'])

# Add currency to a player
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

# Get the balanace of a player
def get_currency(message):
  return("You currently have: " + db[str(message.author.name)] + " currency")

# Find treasure and monsters
def explore(message):
  monsterOrTreasure = random.randint(1, 10)

  if(monsterOrTreasure >= 8):
    monsterSelection = random.randint(1, 3)
    return(selectMonster(monsterSelection))
  else:
    treasureSelection = random.randint(1, 5)
    return(selectTreasure(treasureSelection))

# Select a monster
def selectMonster(num):
  if(num == 1):
    return(monsters[0])
  elif(num == 2):
    return(monsters[1])
  else:
    return(monsters[2])

# Select a treasure
# NEED TO ADD TO PLAYER INVENTORY
def selectTreasure(num):
  if(num == 1):
    return('You found ' + treasure[0])
  elif(num == 2):
    return('You found a ' + treasure[1])
  elif(num == 3):
    return('You found an ' + treasure[2])
  elif(num == 4):
    return('You found ' + treasure[3])
  elif(num == 5):
    return('You found ' + treasure[4])
  
# When the program starts, log the username
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

# Event to get messages from users
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
  if(msg.startswith('.cur') and msg.endswith('explore')):
    await message.channel.send(explore(message))

keep_alive()
client.run(os.getenv('TOKEN'))