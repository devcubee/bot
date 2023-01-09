import os
import json
import discord
from discord.ext import commands

class Client(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().default())

    async def setup_hook(self) -> None:
        for fn in os.listdir("./cogs"):
            if fn.endswith(".py"):
                print(f'Loaded cogs.{fn[:-3]}')
                await self.load_extension(f"cogs.{fn[:-3]}")

    async def on_ready(self):
        print(f'Ready as {self.user}')
        try:
            synced = await self.tree.sync()
        except:
            print('could not sync commands')
        

with open("config.json", "r") as f:
    data = json.load(f)
    TOKEN = data['TOKEN']

client = Client()

client.run(TOKEN)