import discord
from discord.ext import commands
import json
import os
import asyncio
import database

# 載入設定
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"已登入為 {bot.user}")

async def main():
    # 初始化資料庫
    await database.init_db()

    # 載入 cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

    await bot.start(config["token"])

asyncio.run(main())
