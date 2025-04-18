import discord
from discord import app_commands
import json

from src import member_event
from src import server
from src import administrator

# from src import math

try:
    with open("config/config.json", "r") as file:
        config = json.load(file)
        bot_token = config["bot_token"]
        permissions = config["permissions"]
        discord_invite_link = config["discord_invite_link"]
        join_channel_id = config["join_channel_id"]
        leave_channel_id = config["leave_channel_id"]
        boost_channel_id = config["boost_channel_id"]
except FileNotFoundError:
    print("Configuration file not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON from the configuration file.")
    exit(1)


class Bot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = Bot(intents=intents)


@bot.event
async def on_ready():
    print("")
    print(f"Your bot {bot.user} is now RUNNING!")
    print(
        f"Invite link: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions={permissions}&scope=bot%20applications.commands"
    )
    print("")
    await bot.change_presence(activity=discord.Game(discord_invite_link[7:]))


@bot.event
async def on_member_join(member: discord.Member):
    await member_event.on_member_join(member, join_channel_id)


@bot.event
async def on_member_remove(member: discord.Member):
    await member_event.on_member_remove(member, leave_channel_id)


@bot.event
async def on_guild_update(before: discord.Guild, after: discord.Guild):
    await member_event.on_member_update(before, after, boost_channel_id)


administrator.setup(bot)
# math.setup(bot)
server.setup(bot, discord_invite_link)


@bot.tree.command(
    name="help",
    description="Shows this help message.",
)
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="List of all available commands")
    for command in bot.tree.get_commands():
        embed.add_field(
            name=f"/{command.name}",
            value=command.description,
            inline=False,
        )
    await interaction.response.send_message(embed=embed)


bot.run(bot_token, reconnect=True)
