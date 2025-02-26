import discord
from discord.ext import commands
import time
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Initialize the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Global variable to control the reporting process
reporting_active = False

def display_title():
    return "Metaloses Reporting Tool\n-------------------------------"

async def option_one(ctx):
    global reporting_active
    reporting_active = True

    await ctx.send(display_title())
    await ctx.send("Please send your username:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    username_msg = await bot.wait_for("message", check=check)
    username = username_msg.content

    await ctx.send("Please enter your key:")
    key_msg = await bot.wait_for("message", check=check)
    key = key_msg.content

    await ctx.send("Loading...")
    time.sleep(2)

    await ctx.send("Collecting Bots User...")
    time.sleep(5)

    await ctx.send("Reporting Started...")

    total_reports = random.randint(1, 100)
    for i in range(1, total_reports + 1):
        if not reporting_active:
            await ctx.send("Reporting stopped.")
            return
        await ctx.send(f"Report number: {i}")
        time.sleep(0.1)  # Adjust the sleep time if needed to simulate the process

    await ctx.send(f"{total_reports} reports sent.")
    await ctx.send("Thank you for using Hater's Reporting Tool!")

@bot.command(name="increase_og")
async def increase_og(ctx):
    await option_one(ctx)

@bot.command(name="credit")
async def credit(ctx):
    await ctx.send(display_title())
    await ctx.send("You chose option 2: Credit.")
    await ctx.send("Credits: This script was developed by instagram.com/metaloses.")
    await ctx.send("Special thanks to the open-source community!")

@bot.command(name="stop")
async def stop(ctx):
    global reporting_active
    reporting_active = False
    await ctx.send("Reporting process stopped.")

@bot.command(name="exit")
async def exit_bot(ctx):
    await ctx.send("Exiting the program. Goodbye!")
    await bot.close()

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

# Run the bot with the token from the .env file
bot.run(TOKEN)
