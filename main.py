import discord
from discord.ext import commands
import time
import random
from colorama import init, Fore, Style
import os
from dotenv import load_dotenv

# Initialize colorama
init()

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Initialize the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def display_title():
    return f"{Fore.CYAN}Metaloses Reporting Tool{Style.RESET_ALL}\n{Fore.CYAN}-------------------------------{Style.RESET_ALL}"

async def option_one(ctx):
    await ctx.send(display_title())
    await ctx.send(f"{Fore.CYAN}Please send your username: {Style.RESET_ALL}")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    username_msg = await bot.wait_for("message", check=check)
    username = username_msg.content

    await ctx.send(f"{Fore.CYAN}Please enter your key: {Style.RESET_ALL}")
    key_msg = await bot.wait_for("message", check=check)
    key = key_msg.content

    await ctx.send(f"{Fore.YELLOW}Loading...{Style.RESET_ALL}")
    time.sleep(2)

    await ctx.send(f"{Fore.YELLOW}Collecting Bots User...{Style.RESET_ALL}")
    time.sleep(5)

    await ctx.send(f"{Fore.GREEN}Reporting Started...{Style.RESET_ALL}")

    total_reports = random.randint(1, 100)
    for i in range(1, total_reports + 1):
        await ctx.send(f"{Fore.GREEN}Report number: {i}{Style.RESET_ALL}")
        time.sleep(0.1)  # Adjust the sleep time if needed to simulate the process

    await ctx.send(f"{Fore.CYAN}{total_reports} reports sent.{Style.RESET_ALL}")
    await ctx.send(f"{Fore.MAGENTA}Thank you for using Hater's Reporting Tool!{Style.RESET_ALL}")

@bot.command(name="increase_og")
async def increase_og(ctx):
    await option_one(ctx)

@bot.command(name="credit")
async def credit(ctx):
    await ctx.send(display_title())
    await ctx.send(f"{Fore.BLUE}You chose option 2: Credit.{Style.RESET_ALL}")
    await ctx.send(f"{Fore.MAGENTA}Credits: This script was developed by instagram.com/metaloses.{Style.RESET_ALL}")
    await ctx.send(f"{Fore.MAGENTA}Special thanks to the open-source community!{Style.RESET_ALL}")

@bot.command(name="exit")
async def exit_bot(ctx):
    await ctx.send(f"{Fore.RED}Exiting the program. Goodbye!{Style.RESET_ALL}")
    await bot.close()

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}Bot is ready. Logged in as {bot.user}{Style.RESET_ALL}")

# Run the bot with the token from the .env file
bot.run(TOKEN)
