import discord
import os
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

deletejosholinks = True
joshodeletechance = .3
joshotoken = '265655616230522883'
austintoken = '347096530546720768' 
olitude = '311996658508365827'
botid = '598965687855087616'

ggchatid = '1315048346531926016'
testchatid = '1315070155323080765'

hotlines = '''
Suicide Hotline 1+ 800-273-8255 
'''


async def say(text, channel):
    await channel.send(text)


async def roll(m, min, max):
    number = random.randrange(min,max+1)
    await m.channel.send(str(number))

def flip():
    number = random.random()
    if number > .5:
        return True
    else:
        return False

async def kick(interaction: discord.Interaction, member: discord.Member):
    await member.kick()
    await interaction.response.send_message(f"{member.name} has been kicked.")

async def parseCommand(m):
    if 'kick' in m.content:
        for user in m.mentions:
            if str(user.id) in m.content:
                await m.channel.send('kicked: <@' + str(user.id) + '>')
                await discord.Guild.kick(user.id, discord.abc.Snowflake, reason='baka-chan hates you' + message)
        return
    if 'roll' in m.content:
        await roll(m, 1, 20)
        return

    if 'flip' in m.content:
        if flip():
            await say('you got heads', m.channel)
        else:
            await say('you got tails', m.channel)
        return

    if 'hi' in m.content:
        await say('hi!', m.channel)
        return

    if "you're the best" in m.content or "youre the best" in m.content:
        if flip():
            if flip():
                await say('//.//', m.channel)
            else:
                await say('HUH?!', m.channel)
        else: 
            if flip():
                await say('thanks~', m.channel)
            else:
                await say('ありがとうございます~', m.channel)
        return

    else:
        if random.random() < .5:
            await m.channel.send('huh?')
        else:
            await m.channel.send('what?')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(str(message.author) + ': ' + str(message.content))
    if message.author == client.user:
        return

    if random.randrange(1, 6) < .5:
        if 'risk' in message.content:
            await message.channel.send('r-risk... like risk of rain!??!?!')

        if 'damn' in message.content:
            await say('damn fr 😔', message.channel)
         
        if 'kys' in message.content or 'kill yourself' in message.content:
            await say('meanie, be nice, heres this if you need help~' + hotlines, message.channel)

    
    if deletejosholinks:
        if str(message.author.id) == joshotoken and 'http' in message.content:
            if random.random() < joshodeletechance:
                await message.delete()

    if 'baka-chan' in message.content or 'baka chan' in message.content or message.content.endswith('~') or message.content.startswith('&') or botid in message.content:
        await parseCommand(message)
    
    if message.content.startswith('-b') and str(message.author.id) == austintoken:
        out = message.content.split('-b ')
        await message.delete()
        await say(str(out[1]), message.channel)
        # await say(str(out[1]), testchatid)



client.run('TOKEN')


