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
    username = message.author.name
    user_message = message.content
    channel = message.channel.name
    
    # this is really invading user's privacy, dont you think?
    print(f'{username}: {user_message} ({channel})') 

    if message.author == client.user:
        return

    if message.channel.name == 'bot-test':
        if user_message == 'jc!ping':
            start = time.time()
            loading_msg = await message.channel.send(f'Calculating ping...')
            finish = time.time()
            ping_ms = int((finish - start) * 1000)
            await loading_msg.edit(content=f':ping_pong: Pong! in {ping_ms}ms')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Ta-Ta See you later {username}!')
        elif user_message == 'jc!random'
            await loading_msg.edit(content=f'This is your random number: {random.randint(0, 10)}')
 
client.run(TOKEN)   

