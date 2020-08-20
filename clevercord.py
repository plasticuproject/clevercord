'''
Discord bot to chat with Cleverbot. Uses the cleverbotfree library to
communicate via a headless Firefox browser.
Just message "&chat" to chat with Cleverbot.

Copyright (C) 2018  plasticuproject@pm.me

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''

import os
import discord
from discord.ext import commands
from cleverbotfree.cbfree import Cleverbot
import re
from random import randint
from modules.cve import CVE
from modules.discordhelp import DiscordHelp
from modules.password_analyzer import Analyze


bot = commands.Bot(command_prefix='&')
sendCb = Cleverbot().single_exchange

# Discord Bot Token variable
token = os.environ['CLEVERCORD_TOKEN']

# Discord Client ID
clientID = os.environ['CLEVERCORD_CLIENT_ID']


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# uses cleverbotfree to communicate with Cleverbot
@bot.command()
async def chat(ctx, *args):
    print(ctx.message.author)
    print(ctx.message.content)
    userInput = ' '.join(args)
    try:
        response = sendCb(userInput)
        await ctx.send(response)
    except:
        embed = discord.Embed(title='ERROR: Could not connect. Please try again', color=0xff0000)
        await ctx.send(embed=embed)


# search NVD for CVE info
@bot.command()
async def cve(ctx, *args):
    print(ctx.message.author)
    print(ctx.message.content)
    try:
        if len(args) == 0:
            message = '&cve'
        else:
            message = '&cve ' + ' '.join(args)
        result = CVE.cveSearch(message)
        await ctx.send(result)
    except:
        embed = discord.Embed(title='ERROR: Could not connect. Please try again', color=0xff0000)
        await ctx.send(embed=embed)


# analyze password strength
@bot.command()
async def password(ctx, *args):
    print(ctx.message.author)
    print(ctx.message.content)
    try:
        if len(args) == 0:
            message = '&password'
        else:
            message = '&password ' + ' '.join(args)
        result = Analyze.check_password(message)
        if isinstance(result, discord.Embed):
            await ctx.send(embed=result)
        else:
            await ctx.send(result)
    except:
        embed = discord.Embed(title='ERROR: Could not connect. Please try again', color=0xff0000)
        await ctx.send(embed=embed)


# grab a quote from Uncle Ted!
@bot.command()
async def ted(ctx):
    print(ctx.message.author)
    print(ctx.message.content)
    try:
        with open('bomb.txt', 'r') as bomb:
            text = bomb.read()
        r = randint(0,1565)
        s = re.findall("[A-Z].*?[\.!?]", text, re.MULTILINE | re.DOTALL )[r].replace('\n', '').replace('   ', ' ').replace('  ', ' ')
        t = 'Uncle Ted says:\n' + s
        await ctx.send(t)
    except:
        embed = discord.Embed(title='ERROR: Could not connect. Please try again', color=0xff0000)
        await ctx.send(embed=embed)

  
@bot.command()
async def info(ctx):
    embed = discord.Embed(title='cleverbot', description='Cleverbot chatbot.', color=0xeee657)
    
    # give info about you here
    embed.add_field(name='Author', value='plasticuproject#3879')
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name='Server count', value=f'{len(bot.guilds)}')

    # give users a link to invite this bot to their server
    embed.add_field(name='Invite', value='https://discordapp.com/oauth2/authorize?client_id=' + clientID + '&scope=bot')
    await ctx.send(embed=embed)


bot.remove_command('help')


# return command help
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='cleverbot', 
    description='Cleverbot chatbot. List of commands are:', color=0xeee657)
    embed.add_field(name='&chat', value='Have a chat with Cleverbot', inline=False)
    embed.add_field(name='&info', value='Gives a little info about the bot', inline=False)
    embed.add_field(name='&help', value='Gives this message', inline=False)
    embed.add_field(name='&cve', value='Lookup CVEs from NIST NVD', inline=False)
    embed.add_field(name='&password', value='Check estimatied cracking time for passwords', inline=False)
    embed.add_field(name='&ted', value='Uncle Ted\'s greatest hits', inline=False)
    await ctx.send(embed=embed)


bot.run(token)

