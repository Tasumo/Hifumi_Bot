from discord.ext.commands import Bot
from discord import Game
import random

BOT_PREFIX = ("?", "!")
TOKEN = "NDkyMDk3NTkyMjgxNTMwMzg5.DoRv1Q.mjezNefKIaXnTfSDC7WJ0ttGkKo"
client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answer a yes/no question",
                brief="answers from the beyond",
                aliases=['eight_ball', 'eightball', 'eight ball', '8-ball'],
                pass_context = True)
async def eight_ball(context):
    possible_responses= [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely'
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(description='squares a number',
                brief='helps square a number')
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="New Game!!"))
    print("Logged in as " + client.user.name)


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))






    '''
@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/spot?currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is : $" + value)
    '''

client.run(TOKEN)