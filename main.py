from replit import db
from keep_alive import keep_alive
import discord
import requests
import json
import random
import os

# Initialize client object
client = discord.Client()

monsters = ['Bigfoot', 'Chtululu', 'Godzilla', 	"Dragon", "Ogre", "Hydra", "Snake", "Tiki monster", "Yeti"]
treasure = ['Gold', 'Diamond', 'Old Boot', 'Nothing', 'Iron']
weapons = ' Rusty sword \n Ragged tunic \n Old helment \n Cracked shield'

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
    monsterSelection = random.randint(0, len(monsters))
    return(selectMonster(monsterSelection))
  else:
    treasureSelection = random.randint(1, 5)
    return(selectTreasure(treasureSelection))

# Select a monster
def selectMonster(num):
  return('A wild ' + monsters[num] + ' appeared!')

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
  
def helpMessage():
  return('Current Commands: \n.cur meme (Generates a meme) \n.cur inventory (Shows your current inventory and balance) \n.cur explore (Explore for treasure or a monster)')

def fightPlayer(player_name):
  return('You have chosen to fight ' + player_name)

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
  if(msg.startswith('.cur') and msg.endswith('.cur')):
    await message.channel.send('You need to add a function to the end of .cur')
  if(msg.startswith('.cur') and msg.endswith('meme')):
    await message.channel.send(get_meme())
  if(msg.startswith('.cur') and msg.endswith('inventory')):
    await message.channel.send(get_currency(message))
  if(msg.startswith('.cur') and msg.endswith('explore')):
    await message.channel.send(explore(message))
  if(msg.startswith('.cur') and msg.endswith('help')):
    await message.channel.send(helpMessage())
  if(msg.startswith('.cur') and msg.endswith('shop')):
    await message.channel.send(weapons)
  if(msg.startswith('.cur')):
    second_word = msg.split('.cur ', 1)[1]
    if(second_word.startswith('fight')):
      player_name = msg.split('fight ', 1)[1]
      await message.channel.send(fightPlayer(player_name))

keep_alive()
client.run(os.getenv('TOKEN'))