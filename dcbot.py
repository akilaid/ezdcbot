import discord
from discord.ext import commands
import asyncio
from rcon import Client

client = commands.Bot(command_prefix='!')
token = ''
serverip = ""
rconport = ""
rconpass = ""

@client.command()
@commands.has_role("ezAdmin")
async def ez(ctx, arg1, arg2):
    command = str(arg1)
    comoption = str(arg2)
    if "map" == command:
        if "kil" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_killhouse')
            embed=discord.Embed(title="Notification", description="Map changed to **Killhouse**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/SRyfDF6.png")
            await ctx.send(embed=embed)
        elif "cra" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_crash')
            embed=discord.Embed(title="Notification", description="Map changed to **Crash**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/ero2sbB.png")
            await ctx.send(embed=embed)
        elif "shi" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_shipment')
            embed=discord.Embed(title="Notification", description="Map changed to **Shipment**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/2dFN8qx.png")
            await ctx.send(embed=embed)
        elif "rat" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_ratroom_v1')
            embed=discord.Embed(title="Notification", description="Map changed to **Ratroom**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/Uav2Rjm.jpeg")
            await ctx.send(embed=embed)
        elif "bac" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_backlot')
            embed=discord.Embed(title="Notification", description="Map changed to **Backlot**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/dO8wTpS.png")
            await ctx.send(embed=embed)
        elif "blo" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_bloc')
            embed=discord.Embed(title="Notification", description="Map changed to **Bloc**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/kl0M6I6.png")
            await ctx.send(embed=embed)
        elif "bro" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_broadcast')
            embed=discord.Embed(title="Notification", description="Map changed to **Broadcast**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/f4xTvC5.png")
            await ctx.send(embed=embed)
        elif "cro" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_crossfire')
            embed=discord.Embed(title="Notification", description="Map changed to **Crossfire**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/Gxrxpxw.png")
            await ctx.send(embed=embed)
        elif "str" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_strike')
            embed=discord.Embed(title="Notification", description="Map changed to **Strike**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/jnaGXt5.png")
            await ctx.send(embed=embed)
        elif "amb" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_convoy')
            embed=discord.Embed(title="Notification", description="Map changed to **Ambush**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/8IItZD5.png")
            await ctx.send(embed=embed)
        elif "nuk" in comoption:
            with Client((serverip), int(rconport), passwd=(rconpass)) as client:
                response = client.run('map', 'mp_nuketown')
            embed=discord.Embed(title="Notification", description="Map changed to **Nuketown**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/AdqZWXp.png")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Notification", description="**Map not found!**", color=0xfb00ff)
            embed.set_thumbnail(url="https://i.imgur.com/fOdexvd.jpg")
            await ctx.send(embed=embed)
    else:
        print('Done')
    if "gametype" == command:
        with Client((serverip), int(rconport), passwd=(rconpass)) as client:
            response = client.run('gametype', '%s' % (comoption))
        embed=discord.Embed(title="Notification", description="Gametype changed to %s" % (comoption), color=0xb146b9)
        await ctx.send(embed=embed)
    if "rcon" == command:
        with Client((serverip), int(rconport), passwd=(rconpass)) as client:
            response = client.run('status', '%s' % (comoption))
        await ctx.send(response)
@client.command()
async def ezhelp(ctx):
    embed=discord.Embed(title="ezzbn Server Bot",url="https://github.com/akilaid/ezdcbot", description="This bot can be used to change map and gametype of ezzbn cod4 server!", color=discord.Color.red())
    embed.set_thumbnail(url="https://i.imgur.com/nWC5t73.jpg")
    embed.set_author(name="Notification", url="https://github.com/akilaid/ezdcbot", icon_url="https://i.imgur.com/Q0bnBjE.png")
    embed.add_field(name="Administrator Role", value="> • You need **ezAdmin** role to control server using this bot!", inline=False)
    embed.add_field(name="Main command", value="> • Main command is **!ez**. You must use **!ez** before everything", inline=False)
    embed.add_field(name="Changing map", value="> • Use **!ez map <mapname>** to change maps.\n > ∙ ex: !ez map killhouse\n > • Also you can use first 3 letters of map name \n > ∙ ex: !ez map kil", inline=False)
    embed.add_field(name="Changing gametype", value="> • Use **!ez gametype <gametype>** to change gametype\n > ∙ ex: !ez gametype sd ", inline=False)
    embed.add_field(name="Availabe maps", value="> Shipment - mp_shipment \n> Ratroom V1 - mp_ratroom_v1\n> Killhouse - mp_killhouse\n> Nuketown - mp_nuketown", inline=True)
    embed.add_field(name="Available gametypes", value="> Team Deathmatch - war\n> Free-for-all - dm\n> Search & Destroy - sd", inline=True)
    embed.set_footer(text="Developed by _Akila © 2021")
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='You'))
    print('ez Bot started succesfully!')
client.run(token)
