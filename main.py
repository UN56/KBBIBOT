import os
import discord
from discord.ext import commands
from kbbi import KBBI

TOKEN = os.getenv("API_KEY")
intents = discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='/', intents=intents)
kosakata = None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def kbbi(ctx, arg=None):
    if arg == "help":
        await ctx.send("Untuk mencari kosakata gunakan `/kbbi {kosakata}`")
    else:
        try:
            kosakata = KBBI(arg)
            await ctx.send(f"```{kosakata}```")
        except:
            kosakata = f'"{arg}" tidak ditemukan'
            await ctx.send(kosakata)
    print(arg)

client.run(TOKEN)