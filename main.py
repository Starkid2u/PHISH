#!/usr/bin/env/str python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import random

with open("tokenfile", "r") as tokenfile:
    token=tokenfile.read()


async def attachments_to_files(attached,spoiler=False):
    filelist = []
    for i in attached:
        file = await i.to_file()
        filelist.insert(len(filelist),file)
    return filelist
    


my_id = 643638566655754241


client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

helocooldown = 0
guncooldown = 0
gundmg = random.randrange(1, 100, 1)
helo = '_________'
@client.event
async def on_message(message):

    maxhealth = discord.utils.get(message.guild.roles, id = 714534974916919349)
    health9 = discord.utils.get(message.guild.roles, id = 714535185273847871)
    health8 = discord.utils.get(message.guild.roles, id = 714535298729640047)
    health7 = discord.utils.get(message.guild.roles, id = 714535324759621712)
    health6 = discord.utils.get(message.guild.roles, id = 714535348046266449)
    health5 = discord.utils.get(message.guild.roles, id = 714535379675644054)
    health4 = discord.utils.get(message.guild.roles, id = 714535405843775518)
    health3 = discord.utils.get(message.guild.roles, id = 714535436143558788)
    health2 = discord.utils.get(message.guild.roles, id = 714535460860330066)
    health1 = discord.utils.get(message.guild.roles, id = 714535481928319016)
    dead = discord.utils.get(message.guild.roles, id = 714535509279637525)
    scared = discord.utils.get(message.guild.roles, id = 749429015621664790)

    #linking status
    standowner = discord.utils.get(message.guild.members, id = my_id)
    await client.change_presence(status=standowner.status)
    
    if message.author == client.user:
        return

    if message.content.startswith('Phish attack'):
        if not (message.author.id == my_id):
            return
        await message.channel.send('tadeadeadeadeadeadea')
        print(f'attacking {message.mentions[0]}')

    if message.content.startswith('?echo'):
        if not (message.author.id == my_id):
            return
        images = await attachments_to_files(message.attachments,True)
        await message.delete()
        await message.channel.send(message.content[5:],files=images)
        print(f'repeating {message.content[5:]}')

    args = message.content.replace(f"Phish ","")
    argslist = args.split(" ")

    #phish helo code
    global helo
    global helocooldown
    if message.content.startswith('Phish helo'):
        if not (message.author.id == my_id):
            return
        if helocooldown == 1:
            return
        helo = argslist[1]
        await message.channel.send(f"phish helo set to {helo}")
        helocooldown = 1
        await asyncio.sleep(20)
        helocooldown = 0
        return
    if (helo in message.content):
        if message.author.id == 724745445045174334:
            return
        await message.channel.send('daisan no bakudan, PHISH HELO')
        await message.author.add_roles(scared,reason="scared")
        print(f"{message.author.name} is petrified with fear")
        helo = '_______'
        await asyncio.sleep(20)
        print(f"{message.author.name} is no longer scared")
        await message.author.remove_roles(scared,reason="scared")
        await message.channel.send(f"{message.author.mention} you are no longer scared")
        helocooldown = 1
        await asyncio.sleep(30)
        helocooldown = 0
    if scared in message.author.roles:
        await message.delete()

    #phish gun code
    global gundmg
    global guncooldown
    if message.content.startswith('Phish gun'):
        if guncooldown == 1:
            return
        if not (message.author.id == my_id):
            return
        gundmg = random.randrange(1, 100, 1)
        if message.author.id == message.mentions[0].id:
            gundmg = random.randrange(95, 96, 1)
        if gundmg in range(1, 50): #1 damage
            gundmg = 1
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health9,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health8,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        if gundmg in range(51, 75): #2 damage
            gundmg = 2
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health8,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        if gundmg in range(76, 87): #3 damage
            gundmg = 3
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health7,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        if gundmg in range(88, 94): #4 damage
            gundmg = 4
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health6,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
        if gundmg in range(95, 96): #5 damage
            gundmg = 5
            if (maxhealth in message.mentions[0].roles):
                await message.mentions[0].remove_roles(maxhealth,reason="damaged")
                await message.mentions[0].add_roles(health5,reason="damaged")
            elif (health9 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health9,reason="damaged")
                await message.mentions[0].add_roles(health4,reason="damaged")
            elif (health8 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health8,reason="damaged")
                await message.mentions[0].add_roles(health3,reason="damaged")
            elif (health7 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health7,reason="damaged")
                await message.mentions[0].add_roles(health2,reason="damaged")
                
            elif (health6 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health6,reason="damaged")
                await message.mentions[0].add_roles(health1,reason="damaged")
                
            elif (health5 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health5,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
                
            elif (health4 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health4,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
                
            elif (health3 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health3,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
                
            elif (health2 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health2,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")
                
            elif (health1 in message.mentions[0].roles):
                await message.mentions[0].remove_roles(health1,reason="killed")
                await message.mentions[0].add_roles(dead,reason="killed")        
        if gundmg in range(97, 100):
            gundmg = 0
            await message.channel.send("damnit, its a dud")
        if gundmg != 0:
            await message.channel.send(f"you did {gundmg} damage")
        print(f"using PHISH GUN to attack {message.mentions[0].name} for {gundmg} damage")
        guncooldown = 1
        await asyncio.sleep(30)
        guncooldown = 0


client.run(token)