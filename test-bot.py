import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('hello, i am a test bot')

client.run('OTcxODU1ODU1NjY0Mzc3OTM3.YnQlTA.NbqecC4v_Rn2PTOT3mefbjMdnq0')

