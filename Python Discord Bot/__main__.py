import os
from dotenv import load_dotenv
import disnake
from disnake.ext import commands
from disnake import ui


load_dotenv() # Load .env
TOKEN = os.getenv("BOT_TOKEN") # Load secret token from .env


# Set intents
intents = disnake.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=intents) # Bot initialization


# Bot ready
@bot.event
async def on_ready():
    game = disnake.Activity(type=disnake.ActivityType.playing, name="Activity name")
    await bot.change_presence(activity=game, status=disnake.Status.online)
    print("Bot is ready!")


# Simple slash command
@bot.slash_command(name="slash", description="Simple slash command description.")
async def choose_language_message(inter):
    await inter.response.send_message("Hello, World!")


# Simple slash command
@bot.slash_command(name="slash", description="Simple slash command description.")
async def choose_language_message(inter):
    buttons = [
        disnake.ui.Button(label="Button1", style=disnake.ButtonStyle.primary, emoji='🦊', custom_id="slyfox_button"),
        disnake.ui.Button(label="Button2", style=disnake.ButtonStyle.green, emoji='🙀', custom_id="cat_button")
    ]

    await inter.response.send_message("Hello, World!", components=buttons)


# Simple e.on_button_click handler
@bot.event
async def on_button_click(inter):
    # Check the custom ID of the clicked button
    if inter.component.custom_id == "slyfox_button":
        await inter.response.edit_message(content="Button 1 clicked!")
    elif inter.component.custom_id == "cat_button":
        await inter.response.edit_message(content="Button 2 clicked!")