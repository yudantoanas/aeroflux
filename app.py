import datetime
from utils import generateText
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
    scheduler.add_job(
        send_scheduled_pyjokes, 'cron', hour=9, minute=0, args=[testingChannelId])
    scheduler.add_job(
        generateAssignmentAnnouncement, 'cron', hour=10, minute=30, args=[testingChannelId])
    scheduler.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hi!'):
        await message.channel.send("Hello!")
        # await generateAssignmentAnnouncement(int(os.environ.get('TESTING_CHANNEL_ID')))


async def send_scheduled_pyjokes(channel_id):
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send(pyjokes.get_joke())
    else:
        print("Channel not found!")


async def generateAssignmentAnnouncement(channel_id):
    channel = client.get_channel(channel_id)
    res = generateText('data.json')
    await channel.send("**Assignment Announcement**")
    if res:
        await channel.send(res)
            

client.run(os.environ.get('DISCORD_TOKEN'))
