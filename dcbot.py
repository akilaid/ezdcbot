import discord
from discord.ext import commands
import asyncio
from rcon import Client

client = commands.Bot(command_prefix='!')
token = '' #bot token
@client.command()
@commands.has_role("ezAdmin")
async def ez(ctx, arg1, arg2):
    command = str.format(arg1)
    comoption = str.format(arg2)
    if "map" == command:
        with Client('0.0.0.0', 28960, passwd='rconpass') as client:
            response = client.run('map', '%s' % (comoption))
        await ctx.send('Map changed to %s' % (comoption))
    if "gametype" == command:
        with Client('0.0.0.0', 28960, passwd='rconpass') as client:
            response = client.run('gametype', '%s' % (comoption))
        await ctx.send('Gametype changed to %s' % (comoption))
@client.command()
async def ezhelp(ctx):
    embed=discord.Embed(title="ezzbn Server Bot",url="https://blueballfixed.ytmnd.com/", description="This modafakin bot can be used to change map and gametype of ezzbn cod4 server!", color=discord.Color.red())
    embed.set_thumbnail(url="https://i.imgur.com/4YuQ5LF.png")
    embed.set_author(name="Notification", url="https://blueballfixed.ytmnd.com/", icon_url="https://i.imgur.com/Q0bnBjE.png")
    embed.add_field(name="Administrator Role", value="> You need **ezAdmin** role to control server using this bot!", inline=False)
    embed.add_field(name="Main command", value="> Main command is **!ez**. You must use **!ez** before everything", inline=False)
    embed.add_field(name="Changing map", value="> Use **!ez** as primary command and map as secondary command \n > ex: !ez map mp_killhouse ", inline=False)
    embed.add_field(name="Changing gametype", value="> Use **!ez** as primary command and gametype as secondary command \n > ex: !ez gametype sd ", inline=False)
    embed.add_field(name="Availabe maps", value="> Shipment - mp_shipment \n> Ratroom V1 - mp_ratroom_v1\n> Killhouse - mp_killhouse\n> Nuketown - mp_nuketown", inline=True)
    embed.add_field(name="Available gametypes", value="> Team Deathmatch - war\n> Free-for-all - dm\n> Search & Destroy - sd", inline=True)
    embed.set_footer(text="Developed by _RiKuWa © 2021")
    await ctx.send(embed=embed)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='නෝටි දර්ශන'))
    print('ez Bot started succesfully!')
client.run(token)
