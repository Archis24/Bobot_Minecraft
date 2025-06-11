import discord
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

with open('minecraft_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
   
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.command()
async def minerales(ctx):
    mensaje = ""
    for mineral, info in data["minerales"].items():
        mensaje += f"🪨 **{mineral.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n"
        mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
        mensaje += f"⭐ Rareza: {info['rareza']}\n\n"

    await ctx.send(mensaje)

@bot.command()
async def diamantes(ctx):
    info = data["minerales"]["diamantes"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **Diamantes**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command()
async def esmeraldas(ctx):
    info = data["minerales"]["esmeraldas"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **esmeraldas**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command()
async def oro(ctx):
    info = data["minerales"]["oro"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **oro**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command()
async def redstone(ctx):
    info = data["minerales"]["redstone"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **redstone**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(name = "carbon")  # sin tilde aquí
async def carbon(ctx):
    info = data["minerales"]["carbón"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **carbón**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command()
async def hierro(ctx):
    info = data["minerales"]["hierro"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **hierro**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(name="lapislazuli")  # sin tilde aquí
async def lapislazuli_cmd(ctx):
    info = data["minerales"]["lapislázuli"]  # sí con tilde aquí, porque es la clave en JSON
    mensaje = f"🪨 **Lapislázuli**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"
    
    await ctx.send(mensaje)

@bot.command()
async def mundos(ctx):
    mensaje = ""
    for mundo, info in data["mundos"].items():
        mensaje += f"🌍 **{mundo.capitalize()}**\n\n"
    await ctx.send(mensaje)

@bot.command()
async def biomas_overworld(ctx):
    mensaje = ""
    for biomas, info in data["mundos"]["overworld"]["biomas"].items():
        mensaje += f"🌱 **{biomas.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n\n"

    await ctx.send(mensaje)  # Envía cada parte por separado

@bot.command()
async def biomas_nether(ctx):
    mensaje = ""
    for biomas, info in data["mundos"]["nether"]["biomas"].items():
        mensaje += f"🌱 **{biomas.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n\n"

    await ctx.send(mensaje)  # Envía cada parte por separado

@bot.command()
async def biomas_end(ctx):
    mensaje = ""
    for biomas, info in data["mundos"]["end"]["biomas"].items():
        mensaje += f"🌱 **{biomas.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n\n"

    await ctx.send(mensaje)

@bot.command()
async def mobs(ctx):
    mensaje = ""
    overworld_mobs = data["mundos"]["overworld"]["mobs"]
    
    for tipo, mobs in overworld_mobs.items():  # tipo será "hostil" o "pasivos"
        mensaje += f"🐶 **{tipo.capitalize()}**:\n"
        for mob, info in mobs.items():
            mensaje += f"🐾 **{mob.capitalize()}**\n"
            mensaje += f"📜 Descripción: {info['descripcion']}\n"
            mensaje += f"💔 Vida: {info['vida']}\n"
            mensaje += f"⚔️ Daño: {info['daño']}\n\n"

    await ctx.send(mensaje)


    


TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)