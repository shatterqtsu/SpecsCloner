# Discord Server Cloner
# Created By Specs#3366
# discord.gg/fort

import psutil
from pypresence import Presence
import time
import sys
import os
import discord
import asyncio
import colorama
import platform
from colorama import Fore, init, Style
from utilities import Clone

client = discord.Client()

os.system("cls & title [Server Cloner] - Created By Specs#3366")

print(f"""
     
░██████╗██████╗░███████╗░█████╗░░██████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝
╚█████╗░██████╔╝█████╗░░██║░░╚═╝╚█████╗░
░╚═══██╗██╔═══╝░██╔══╝░░██║░░██╗░╚═══██╗
██████╔╝██║░░░░░███████╗╚█████╔╝██████╔╝
╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═════╝░

       Created By Specs#3366/Returing To DDosing/Hacking soon... | discord.gg/fort
       
            """)

guild_s = input('[+] Input Guild ID To Copy: ')
guild = input('[+] Input Guild ID To Paste: ')
token = input(f'[+] Input Token: ')
corpse1 = guild_s 
corpse2 = guild  
token = token 

@client.event
async def on_ready():
    extrem_map = {}
    print()
    print(f"Logged In As: {client.user}")
    print("Attempting To Clone Server...")
    print()
    guild_from = client.get_guild(int(corpse1))
    guild_to = client.get_guild(int(corpse2))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    await asyncio.sleep(.05)
    os._exit(0)
    


client.run(token, bot=False)