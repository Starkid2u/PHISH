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

    if message.channel.category.id == 736788095667666985:
        return
    
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

    global helo
    if message.content.startswith('helo'):
        helo == message.content
        await message.channel.send(helo)

    if (helo in message.content):
        await message.channel.send('test')


client.run(token)