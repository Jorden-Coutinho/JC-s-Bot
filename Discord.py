import discord
from discord.ext import commands
import random
import time
from discord.ext import commands
import json
import requests
from discord import message
from discord import channel
from discord import Embed
TOKEN = 'OTMyMjg3MzM5NzA1ODI3MzM5.YeQyPg.l5-LEo-vhLBT1MjQmeP3fzg9Cgk'
DDLOGO = 'data:image/png;base64,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'

client = commands.Bot(command_prefix = "b!")

async def fake_user_send(
    ctx: commands.Context, text: str, name: str, avatar_url: str
) -> None:
    """
    Sends a message via a webhook to make it look like it was a real user that did.

    Parameters:
        ctx: The context of the command.
        text: The text to send.
        name: The name of the webhook.
        avatar_url: The avatar URL of the webhook. Must be valid as the webhook
                    creation process will fail if it is not.
    """

    # Create an webhook if it doesn't exist, so we don't have create a new
    # webhook every time we call this.
    webhook: discord.Webhook = None
    channel_webhooks = await ctx.channel.webhooks()
    if not list(filter(lambda w: w.name == name, channel_webhooks)):
        webhook = await ctx.channel.create_webhook(
            name=name, avatar=bytes(requests.get(avatar_url).content)
        )
    else:
        webhook = list(filter(lambda w: w.name == name, channel_webhooks))[0]

    await webhook.send(text)

@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))

coins = 0

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

    elif user_message.lower() == 'b! bal':
        em = discord.Embed(title = f"{username}'s Balance" , color = discord.Color.teal())
        em.add_field(name = "Wallet",value = "0", inline=False)
        em.add_field(name = "Bank",value = "0",inline=False)
        await message.channel.send(embed=em)
         
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
      await fake_user_send("What now??", "Jorden Coutinho", DDLOGO)
    
    elif 'sz_skill' in message.content:
      await fake_user_send("What now??", "sz_skill", DDLOGO)

    elif 'Jorden' in message.content:
      await fake_user_send("What now??", "Jorden Coutinho", DDLOGO)

    elif message.content == 'jorden':
      await fake_user_send(":skull:", "Jorden Coutinho", DDLOGO)

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

    elif user_message.lower() == 'b!commands':
        await message.channel.send(f'**All Bili Commands in detail** \n\t**b! beg:** Has a 0.000% chance to get Coins\n\t**b! fish:** Has a 100% to........... not get anything.\n\t**b! mine:** A useless command all you get is scammed.\n\t**b! work:** You are the first person to try to go to work without having any.\n\t**b! ping:** Tells you the bots latency and response time.\n\t**b! bye:** Just say it before you go offline\n\t**b! bal:** Used to see your coins. (Yes the same coins which you dont have)\n\t**b! commands:** Takes you here ')        
     
    elif user_message.lower() == 'b!roll 50':
        await message.reply(content=f'This is your random number {random.randint(0, 50)}')

    elif user_message.lower() == 'b!donate':
        await message.channel.send(f'Please tell what is your message if any and what do you want to sponsor (e.g. Events, Giveaway) our staff team will reach to you soon \n\n\t\t <@!759066319735226380> <@&931478734291230810>')
    
    elif 'bad server' in message.content:
      await message.channel.send(f'Did you just call this server bad? Shame on you')
    
    elif user_message.lower() == 'b! botinfo':
        em = discord.Embed(title = f"Bili Bot Info" , color = discord.Color.gold())
        em.add_field(name = "Bot Team",value = "JC |#6241  and sz_skill\#5551", inline=False)
        em.add_field(name = "Partners",value = "Gamer's Galaxy (Server)",inline=False)
        await message.channel.send(embed=em)
    


@client.event
async def on_message_edit(before,after):
    em = discord.Embed(title = f"{before.author} edited a message", color = discord.Color.blue())
    em.add_field(name = "Before",value = before.content )
    em.add_field(name = "After",value = after.content, )
    await after.channel.send(embed=em)
    
member = discord.member 
client.run(TOKEN)
