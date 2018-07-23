'''
Discord bot to chat with Cleverbot. Uses the cleverbotfree library to <br />
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

import discord
from discord.ext import commands
from cleverbotfree.cbfree import Cleverbot

bot = commands.Bot(command_prefix='&')
sendCb = Cleverbot().single_exchange


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# uses cleverbotfree to communicate with Cleverbot
@bot.command()
async def chat(ctx, userInput):
    try:
        response = sendCb(userInput)
        await ctx.send(response)
    except:
        embed = discord.Embed(title='ERROR: Could not connect. Please try again',
                               color=0xff0000)
        await ctx.send(embed=embed) 


    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title='cleverbot', description='Cleverbot chatbot.',
                          color=0xeee657)
    
    # give info about you here
    embed.add_field(name='Author', value='<...>')
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name='Server count', value=f'{len(bot.guilds)}')

    # give users a link to invite this bot to their server
    embed.add_field(name='Invite', 
     value='https://discordapp.com/oauth2/authorize?client_id=<...>&scope=bot')

    await ctx.send(embed=embed)

bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='cleverbot', 
    description='Cleverbot chatbot. List of commands are:', color=0xeee657)
    embed.add_field(name='&chat', value='Have a chat with Cleverbot', 
                    inline=False)
    embed.add_field(name='&info', value='Gives a little info about the bot', 
                    inline=False)
    embed.add_field(name='&help', value='Gives this message', inline=False)

    await ctx.send(embed=embed)

bot.run('<...>')
