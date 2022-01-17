import discord
import random
import time

TOKEN = 'OTMyMjg3MzM5NzA1ODI3MzM5.YeQyPg.l5-LEo-vhLBT1MjQmeP3fzg9Cgk'

client = discord.Client()

@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = message.author.username
    user_message = message.content
    channel = message.channel.name
    
    # this is really invading user's privacy, dont you think?
    print(f'{username}: {user_message} ({channel})') 

    if message.author == client.user:
        return

    if message.channel.name == 'bot-test':
        if user_message.lower() == 'jc!ping':
            start = time.time()
            loading_msg = await message.channel.send(f'Calculating ping...')
            finish = time.time()
            ping_ms = int((finish - start) * 1000)
            await loading_msg.edit(content=f':ping_pong: Pong! Ping is {ping_ms}ms')
            
            return 
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Ta-Ta See you later {username}!')
            return

client.run(TOKEN)   
