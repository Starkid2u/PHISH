#!/usr/bin/env/str python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio

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

helo = '_________'
@client.event
async def on_message(message):

    scared = discord.utils.get(message.guild.roles, id = 749429015621664790)

    if message.author == client.user:
        return

    if message.content.startswith('Phish attack'):
        if (message.author.id == my_id):
            await message.channel.send('tadeadeadeadeadeadea')
            print(f'attacking {message.mentions[0]}')

    if message.content.startswith('?echo'):
        if (message.author.id == my_id):
            images = await attachments_to_files(message.attachments,True)
            await message.delete()
            await message.channel.send(message.content[5:],files=images)
            print(f'repeating {message.content[5:]}')

    args = message.content.replace(f"phish ","")
    argslist = args.split(" ")

    global helo
    if message.content.startswith('phish helo'):
        helo = argslist[1]
        await message.channel.send(helo)
        return

    if (helo in message.content):
        if message.author.id == 724745445045174334:
            return
        await message.channel.send('daisan no bakudan, PHISH HELO')
        await message.author.add_roles(scared,reason="scared")
        print(f"{message.author.name} is petrified with fear")
        await asyncio.sleep(20)
        print(f"{message.author.name} is no longer scared")
        await message.author.remove_roles(scared,reason="scared")
        await message.channel.send(f"{message.author.mention} you are no longer scared")
        helo = '_______'


client.run(token)