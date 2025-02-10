import os
import discord
import pyjokes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv(override=True)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    testingChannelId = int(os.environ.get('TESTING_CHANNEL_ID'))
    scheduler.add_job(send_scheduled_pyjokes, 'interval', seconds=1, args=[testingChannelId])
    scheduler.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hi!'):
        await message.channel.send('Hello!')

async def send_scheduled_pyjokes(channel_id):
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send(pyjokes.get_joke())
    else:
        print("Channel not found!")

client.run(os.environ.get('DISCORD_TOKEN'))