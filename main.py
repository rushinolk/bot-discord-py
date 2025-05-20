import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Dic está aprontando")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1372981097800929333)
    await canal.send(f"{membro.mention} entrou no servidor, acabou a farra")

@bot.event
async def on_member_remove(membro:discord.Member):
    canal = bot.get_channel(1372985552114155530)
    await canal.send(f"{membro.mention} foi eliminado")

# ctx é o contexto em que a funação é chamada abrangendo todos os dados do evento
@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.mention
    await ctx.send(f"Koe {nome}, tranquilidade?")


# Manter no final
bot.run(token)  

