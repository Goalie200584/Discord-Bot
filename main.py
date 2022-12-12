import os
import discord
import requests
import json
from keep_alive import keep_alive
import random
from discord.ext import commands
import typing as t


client = commands.Bot(command_prefix = '.')





evanid = '<@763201251717414942>'
tylerid = '<@318831677789175808>'

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('We have Logged in as {0.user}' .format(client))




@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('/dababy'):
    await message.channel.send('LESSSS GOOOO')

  if message.content.startswith('/inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('/idontcare'):
    await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
  
  if message.content.startswith('/evan'):
    for i in range(2):
      await message.channel.send (evanid)
    
  if message.content.startswith('/tyler'):
    for i in range(5):
      await message.channel.send (tylerid)

  if message.content.startswith('/bedgame'):
    await message.channel.send("@everyone Does anyone wanna play THE BEDGAME?")
    
  if message.content.startswith('/pufferboi'):
     await message.channel.send('https://www.youtube.com/watch?v=qKxfWd79HFI')
  if message.content.startswith ('/nice'):
     await message.channel.send ('Your dad is very nice' + tylerid)
  
  if message.content.startswith('/niceevan'):
     await message.channel.send('Your dad is very nice' + evanid)
     
  if message.content.startswith('/ah ok'):
     await message.channel.send(tylerid + ' loves ice cream')

  if message.content.startswith('/ideas'):
      await message.channel.send('@everyone What do you want the Bot to do?')
  


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()





keep_alive()
client.run(os.getenv('key')) 





#if message.content.startswith('/random'):
  #  songs = random.randint(1,3)
   # if (songs == 1):
  #    await message.channel.send('-play i just had sex')
  #if (songs == 2):
   # await message.channel.send ('-play your a wizard harry')
  #if (songs == 3):
   # await message.channel.send('-play i got bitches')



