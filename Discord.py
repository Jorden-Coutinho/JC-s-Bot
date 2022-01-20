from email import message
from importlib.resources import contents
from socket import MSG_CMSG_CLOEXEC, MSG_NOTIFICATION
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
    

    if message.author == client.user:
        return

    if message.channel.name == 'bot-test':
        if user_message == 'b! ping':
            start = time.time()
            loading_msg = await message.channel.send(f'Calculating ping...')
            finish = time.time()
            ping_ms = int((finish - start) * 1000)
            await loading_msg.edit(content=f':ping_pong: Pong! in {ping_ms}ms')
        elif user_message.lower() == 'b! bye':
            await message.channel.send(f'Ta-Ta See you later {username}!')
        elif user_message == 'b! random':
                await message.reply(content=f'This is your random number {random.randint(0, 10)}')

user_message = MSG_NOTIFICATION.content
if user_message == 'b!beg':
    MSG_CMSG_CLOEXEC.edit(content=f'No coins for you LOL') 
client.run(TOKEN)   
