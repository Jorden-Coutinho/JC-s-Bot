from importlib.resources import contents
import discord
from discord.ext import commands
import random
import time
from discord.ext import commands
import json

TOKEN = 'OTMyMjg3MzM5NzA1ODI3MzM5.YeQyPg.l5-LEo-vhLBT1MjQmeP3fzg9Cgk'

client = discord.Client()

@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))

x = 1

@client.event
async def on_message(message):
    username = message.author.name
    user_message = message.content
    channel = message.channel.name
    
    txt = message.content

    if message.author == client.user:
        return

    if message.content.startswith('b! ping'):
        start = time.time()
        loading_msg = await message.channel.send(f'Calculating ping...')
        finish = time.time()
        ping_ms = int((finish - start) * 1000)
        await loading_msg.edit(content=f':ping_pong: Pong! in {ping_ms}ms')
    
    elif user_message.lower() == 'b! bye':
        await message.channel.send(f'Ta-Ta See you later {username}!')
    
    elif user_message == 'b! roll 10':
        await message.reply(content=f'This is your random number {random.randint(0, 10)}')
    
    elif user_message.lower() == 'b! beg':
        await message.channel.send(f'No Money for you loser {username}!')

    elif user_message.lower() == 'b! fish':
        await message.channel.send(f'You dont even know how to fish HaHaHa {username}!')

    elif user_message.lower() == 'b! mine':
        await message.channel.send(f'You cant mine with ur hands LOL {username}!')

    elif user_message.lower() == 'b! work':
        await message.channel.send(f'Go get a job first {username}!')

    elif user_message.lower() == 'b! help':
        await message.channel.send(f'> All Commands\n\n b! beg💵 \n\n b! fish🎣 \n\n b! mine⛏️ \n\n b! work💼 \n\n b! ping🏓 \n\n b! bye👋\n\n b! bal 🪙\n\n b! commands > ')
        
    elif user_message.lower() == 'b! hunt':
        await message.channel.send(f'Cant shoot with ur fingers u aint spiderman either {username}!')

    elif user_message.lower() == 'b! bal':
        await message.channel.send(f' > {username}\'s Balance\nCash: 00\nBank: 00\nJust go and beg')
    
    elif user_message.lower() == 'b! commands':
        await message.channel.send(f'**All Bili Commands in detail** \n\t**b! beg:** Has a 0.000% chance to get Coins\n\t**b! fish:** Has a 100% to........... not get anything.\n\t**b! mine:** A useless command all you get is scammed.\n\t**b! work:** You are the first person to try to go to work without having any.\n\t**b! ping:** Tells you the bots latency and response time.\n\t**b! bye:** Just say it before you go offline\n\t**b! bal:** Used to see your coins. (Yes the same coins which you dont have)\n\t**b! commands:** Takes you here ')        
     
    elif user_message.lower() == 'b! roll 50':
        await message.reply(content=f'This is your random number {random.randint(0, 50)}')

    elif user_message.lower() == 'b! donate':
        await message.channel.send(f'Please tell what is your message if any and what do you want to sponsor (e.g. Events, Giveaway) our staff team will reach to you soon \n\n\t\t <@!759066319735226380> <@&931478734291230810>')
    
    elif txt == 'pls rob':
        await message.channel.send(f'Haha good to see you try but robbing is not allowed here')

    elif message.content.startswith('pls rob'):
        await message.channel.send(f'Haha good to see you try but robbing is not allowed here')
    
    elif message.content.startswith('pls heist'):
        await message.channel.send(f'Haha good to see you try but robbing is not allowed here in my server earn your own cash rather than robbing someone elses')
    
    elif 'jorden' in message.content:
      await message.channel.send(f'What now??')
    
    elif 'Jorden' in message.content:
      await message.channel.send(f'What now??')

    elif message.content == 'jorden':
      await message.add_reaction('☠️')

    if message.content.startswith('b!ping'):
        start = time.time()
        loading_msg = await message.channel.send(f'Calculating ping...')
        finish = time.time()
        ping_ms = int((finish - start) * 1000)
        await loading_msg.edit(content=f':ping_pong: Pong! in {ping_ms}ms')
    
    elif user_message.lower() == 'b!bye':
        await message.channel.send(f'Ta-Ta See you later {username}!')
    
    elif user_message == 'b!roll 10':
        await message.reply(content=f'This is your random number {random.randint(0, 10)}')
    
    elif user_message.lower() == 'b!beg':
        await message.channel.send(f'No Money for you loser {username}!')

    elif user_message.lower() == 'b!fish':
        await message.channel.send(f'You dont even know how to fish HaHaHa {username}!')

    elif user_message.lower() == 'b!mine':
        await message.channel.send(f'You cant mine with ur hands LOL {username}!')

    elif user_message.lower() == 'b!work':
        await message.channel.send(f'Go get a job first {username}!')

    elif user_message.lower() == 'b!help':
        await message.channel.send(f'> All Commands\n\n b! beg💵 \n\n b! fish🎣 \n\n b! mine⛏️ \n\n b! work💼 \n\n b! ping🏓 \n\n b! bye👋\n\n b! bal 🪙\n\n b! commands > ')
        
    elif user_message.lower() == 'b!hunt':
        await message.channel.send(f'Cant shoot with ur fingers u aint spiderman either {username}!')

    elif user_message.lower() == 'b!commands':
        await message.channel.send(f'**All Bili Commands in detail** \n\t**b! beg:** Has a 0.000% chance to get Coins\n\t**b! fish:** Has a 100% to........... not get anything.\n\t**b! mine:** A useless command all you get is scammed.\n\t**b! work:** You are the first person to try to go to work without having any.\n\t**b! ping:** Tells you the bots latency and response time.\n\t**b! bye:** Just say it before you go offline\n\t**b! bal:** Used to see your coins. (Yes the same coins which you dont have)\n\t**b! commands:** Takes you here ')        
     
    elif user_message.lower() == 'b!roll 50':
        await message.reply(content=f'This is your random number {random.randint(0, 50)}')

    elif user_message.lower() == 'b!donate':
        await message.channel.send(f'Please tell what is your message if any and what do you want to sponsor (e.g. Events, Giveaway) our staff team will reach to you soon \n\n\t\t <@!759066319735226380> <@&931478734291230810>')
    
    elif 'bad server' in message.content:
      await message.channel.send(f'Did you just call this server bad? Shame on you')
    
    elif user_message == 'b!spam':
      while x == 1:
        await message.channel.send(f'Spam')





    @client.event
    async def on_message_edit(before,after):
        em = discord.Embed(title = f"{before.author} edited a message", color = discord.Color.blue())
        em.add_field(name = "Before",value = before.content)
        em.add_field(name = "After",value = after.content)
        await message.channel.send(em)

member = discord.member 
client.run(TOKEN)
