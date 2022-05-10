import discord

from discord.ext import commands

client = commands.Bot(command_prefix='!')
@client.commands()
async def hello(ctx, arg1, arg2):
    await ctx.send('This is arg1' + arg1 + 'This is arg2' + arg2)


client.run('OTcxODU1ODU1NjY0Mzc3OTM3.YnQlTA.NbqecC4v_Rn2PTOT3mefbjMdnq0')
