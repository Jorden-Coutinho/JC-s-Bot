from email import message
import discord
import random

TOKEN = 'OTMyMjg3MzM5NzA1ODI3MzM5.YeQyPg.l5-LEo-vhLBT1MjQmeP3fzg9Cgk'

client = discord.Client()

@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})') 

if message.author == client.user:
    return

if message.channel.name == 'bot-test':
    if user_message.lower() == 'ping':
        await message.channel.send(f'pong🏓 {username}!')
        return 
    elif user_message.lower() == 'bye':
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == 'random'
client.run(TOKEN)