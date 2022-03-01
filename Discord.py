import discord
from discord.ext import commands
import random
import time
from discord.ext import commands
import json
from discord import message
from discord import channel
from discord import Embed
TOKEN = 'OTMyMjg3MzM5NzA1ODI3MzM5.YeQyPg.l5-LEo-vhLBT1MjQmeP3fzg9Cgk'

client = commands.Bot(command_prefix = "b!")

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
      await message.channel.send(f'What now??')
    
    elif 'sz_skill' in message.content:
      await message.channel.send(f'What now?? I am Busy ~sz_skill')

    elif 'Jorden' in message.content:
      await message.channel.send(f'What now??')

    elif message.content == 'jorden':
      await message.channel.send('+:skull:')

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


await fake_user_send(ctx, "Hello!", "your name", "avatar url")
    
member = discord.member 
client.run(TOKEN)
