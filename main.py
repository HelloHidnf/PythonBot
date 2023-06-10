from keep_alive import keep_alive
import time
import discord
from discord import Member
import discord.utils
from discord.ext import commands
from discord.utils import get
from typing import Optional
from random import randint
import os

c = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes - definitely.", "You may rely on it."]

V = 0.5

client = commands.Bot(command_prefix='.', help_command = None)

@client.event
async def on_ready():
  print('connected to {0.user}'.format(client))
  await client.change_presence(activity = discord.Game(f'Web bot version {V}'))

#macro list
@client.command()
async def macros(ctx):
  embed = discord.Embed(title = 'Macros',
  description = '.macros\n.creator\n.test\n.mention @user\n.cry\n.say (very cool supreme helpers only)\n.8ball',
  colour = discord.Colour.from_rgb(0, 255, 200)
  )
  embed.set_footer(text = 'The current preset is .')
  try:
    await ctx.message.author.send(embed=embed)
  except:
    await ctx.send(f"{ctx.message.author.mention} your dm's aren't open, I will send them here instead")
    await ctx.send(embed=embed)
  await ctx.message.delete()

#links
@client.command()
async def creator(ctx):
  embed = discord.Embed(title = 'Creator of this bot',
  description = 'YouTube. https://www.youtube.com/channel/UChMrrmwVdde88CIV4ZH0_rw\n\nTwitch.   https://www.twitch.tv/hellohidnf1',
  colour = discord.Colour.from_rgb(0, 255, 200)
  )
  embed.set_author(name = 'HelloHidnf',
  icon_url = 'https://cdn.discordapp.com/attachments/982948066082574346/990371880361934968/HelloHidnf.webp')
  await ctx.send(embed=embed)
  await ctx.message.delete()

#test
@client.command()
async def test(ctx):
  await ctx.send('success')
  await ctx.message.delete()
	
#mention test
@client.command()
async def mention(ctx, member: Member, *, reason: Optional[str] = 'no reason!'):
  if  member.mention == '<@836301182175281214>':
    await ctx.send(f'{ctx.message.author.mention}, why would you @ me for {reason}')
    await ctx.message.add_reaction('😡')
  else:
    await ctx.send(f'{ctx.message.author.mention} has just {member.mention} for {reason}')
    await ctx.message.delete()

#X's cry request
@client.command()
async def cry(ctx):
  await ctx.send(f'{ctx.message.author.mention} made me cry')
  await ctx.message.add_reaction('😭')

#repeats anything put after the command
@client.command()
@commands.has_role("very cool supreme helpers")
async def say(ctx, *, message):
  await ctx.send(message)
  await ctx.message.delete()

#8ball
@client.command(name='8ball')
async def _8ball(ctx, * , message):
  N = randint(0, 19)
  await ctx.send(f"'{message}' - {ctx.message.author.mention}\n`{c[N]}`")
  await ctx.message.delete()

#command doesn't exist
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, discord.ext.commands.errors.CommandNotFound):
    await ctx.message.add_reaction('😑')
    msg = await ctx.send('This does not appear to be a command, please type .macros to see available commands')
    time.sleep(5)
    await ctx.message.delete()
    await msg.delete()

keep_alive()

client.run(os.getenv('token'))