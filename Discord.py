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
import asyncio
TOKEN = 'OTMyMjg3MzM5NzA1ODI3MzM5.YeQyPg.l5-LEo-vhLBT1MjQmeP3fzg9Cgk'
DDLOGO = 'https://cdn.discordapp.com/avatars/865160569303859240/a0c2a9ab448add501668d2146e1b35f6.jpg?size=1024'
JCLOGO = 'https://media.discordapp.net/attachments/939394240633507850/948151775125446676/Copy_of_Watermark_1619326314525.png?width=657&height=657'

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
        em.add_field(name = "Wallet",value = "69", inline=False)
        em.add_field(name = "Bank",value = "0", inline=False)
        em.add_field(name = "💀", value = "Never Gonna Give you up", inline=True)
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
      await fake_user_send(message, "What now??", "Jorden Coutinho", JCLOGO)
    
    elif 'sz_skill' in message.content:
      await fake_user_send(message, "What now??", "sz_skill", DDLOGO)
    
    elif message.content == 'jorden':
      await fake_user_send(message, ":skull:", "Jorden Coutinho", JCLOGO)

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

    
     
    elif user_message.lower() == 'b!roll 50':
        await message.reply(content=f'This is your random number {random.randint(0, 50)}')

    elif user_message.lower() == 'b!donate':
        await message.channel.send(f'Please tell what is your message if any and what do you want to sponsor (e.g. Events, Giveaway) our staff team will reach to you soon \n\n\t\t <@!759066319735226380> <@&931478734291230810>')
    
    elif 'bad server' in message.content:
      await message.channel.send(f'Did you just call this server bad? Shame on you')
    
    elif user_message.lower() == 'b! botinfo':
        em = discord.Embed(title = f"Bili Bot Info" , color = discord.Color.gold())
        em.add_field(name = "Bot Team",value = "Jorden Coutinho#6241  and sz_skill\#5551", inline=False)
        em.add_field(name = "Partners",value = "Gamer's Galaxy (Server)",inline=False)
        await message.channel.send(embed=em)
    
    elif user_message in ("GTN", "b! egtn", "B! egtn", "b! eGTN" ):
        pass
        number = random.randint(1, 10)
        await message.channel.send('Guess the number I am thinking of')

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        msg = await client.wait_for("message", check=check)

        if int(msg.content) == number:
            await message.channel.send("You got it right!!")
        else:
            await message.channel.send(f"Nope it was **{number}**")

    elif user_message == ("b! beg"):
        await channel.message.send(f"#rickroll here")

    elif user_message == ("bmr"):
        em = discord.Embed(title = f"Mod Rules" , color = discord.Color.blue())
        em.add_field(name = "Please read carefully",value = " 1. There is a mod only channel which you shall get access to soon if you are reading these rules, use it to log any things which happened in the server every 48 hours (at maximum)\n\n 2️. Please do not give any free roles to anyone without asking me, unless they need it (not want, need) and remove it as soon as the work is done\n\n 3️. If you would like to ban someone or kick for a good reason please do then dm me the reason, instead of kicking or banning them\n\n 4️. You should moderate and help the members whenever you can.\n\n 5️. If you tell any member to stop doing something which is against the rules but they do not stop take action against them such as warn, timeout. \n\t DM me if you need more help",inline=False)
        await message.channel.send(embed=em)

    elif user_message == ("b!tag spamming"):
        await message.channel.send("Spamming: Sending the same message indiscriminately to (a large number of internet users) is known as spamming.")

@client.event
async def on_message_edit(before,after):
    em = discord.Embed(title = f"{before.author} edited a message", color = discord.Color.blue())
    em.add_field(name = "Before",value = before.content )
    em.add_field(name = "After",value = after.content, )
    await after.channel.send(embed=em)


    

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = "b!", intents=intents)

@bot.event
async def on_member_remove(member):
    leave_channel = bot.get_channel(934387502083612702)
    modchannel = bot.get_channel(933966074955833445)
    em = discord.Embed(title = f"Goodbye Message" , color = discord.Color.gold())
    em.add_field(name = "Bye", value = "{member.mention} has left the server :sob:", inline=False)

    try:
        await member.send(f"Hey {member.display_name}! goodbye")
    except:
        await modchannel.send(f"{member.mention} I can't dm you, but goodbye")
        
"""
on_member_ban
on_member_join
on_member_remove
on_member_unban
on_member_update
"""


member = discord.member 
client.run(TOKEN)
