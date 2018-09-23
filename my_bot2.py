from discord.ext import commands
import math
import discord
import random

BOT_PREFIX = ("?", "!")
TOKEN = "NDkyMDk3NTkyMjgxNTMwMzg5.DoRv1Q.mjezNefKIaXnTfSDC7WJ0ttGkKo"
client = commands.Bot(command_prefix=BOT_PREFIX)


@client.command(description="Words of advice from Hifumi", pass_context=True, brief="Answers from the anime gods")
async def advice(context):
    possible_advice = [
        'The early bird gets the worm, but the second mouse gets the cheese.',
        'Be on the alert to recognize your prime at whatever time of your life it may occur.',
        'Your road to glory will be rocky, but fulfilling.',
        'Courage is not simply one of the virtues, but the form of every virtue at the testing point.',
        'Patience is your alley at the moment. Don’t worry!',
        'Nothing is impossible to a willing heart.',
        'Don’t worry about money. The best things in life are free.',
        'Nothing is so much to be feared as fear.'
    ]
    await client.say(random.choice(possible_advice) + ", " + context.message.author.mention)


@client.command(name='8ball',
                description="Answer a yes/no question",
                brief="answers from the beyond",
                aliases=['eight_ball', 'eightball', 'eight ball', '8-ball'],
                pass_context=True)
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


@client.command(description='Ping Pong!',  brief='Ping Pong')
async def ping():
    await client.say('Pong!')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="New Game!!"))
    print("Logged in as " + client.user.name)


@client.command(description='sends a picture of a waifu', brief='sends a picture of waifu :D')
async def waifu():
    channel_id = discord.Object(492089529080086530)
    image_number = random.randint(1, 7)
    directory = ".\\images\\" + str(image_number) + '.png'
    await client.send_file(channel_id, directory)


client.run(TOKEN)



