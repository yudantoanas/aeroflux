import os
import discord
import os
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    scheduler.add_job(send_scheduled_message, 'interval', seconds=5)
    scheduler.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello,'):
        await message.channel.send('Hello!')

async def send_scheduled_message():
    channel_id = 1338359801608142919  # Replace with your channel ID
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send(f"📢 Scheduled message! The current time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("⚠️ Channel not found!")

client.run(TOKEN)