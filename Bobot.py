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

@bot.command(help="Lista de comandos disponibles")
async def ayuda(ctx):
    mensaje = "📜 **Lista de comandos disponibles:**\n\n"
    for comando in bot.commands:
        mensaje += f"🔹 **{comando.name}**: {comando.help}\n"
    await ctx.send(mensaje)
    
    

@bot.command(help="Instrucciones para completar Minecraft")
async def completar(ctx):
    
    await ctx.send("1. 🪓 Sobrevive y reúne recursos: Crea herramientas de piedra 🪨, recolecta alimentos 🍖 y carbón 🪵. Busca hierro ⚙️ para mejores armas ⚔️ y armaduras 🛡️.\n"
    "2. 💎 Consigue diamantes: Ve a las capas profundas ⛏️ (-59) para minar diamantes 💎 y obsidiana 🔲 (para el portal al Nether).\n"
    "3. 🔥Viaja al Nether: Busca fortalezas 🏰 para conseguir varas de Blaze🔥 y busca en las warped forests endermans para obtener ender pearls🧿.\n"
    "4.🧿 Haz Ojos de Ender: Combina perlas de Ender 🧿 con polvo de Blaze 🔥.\n"
    "5. 🧭Encuentra la Fortaleza: Usa los Ojos de Ender para localizar la Fortaleza en el Overworld.\n"
    "6. 🐉 Derrota al Dragón: En el End, destruye los cristales de curación 🔮 y vence al Ender Dragon 🐉⚔️.\n"
    "7. Explora el End(opcional): Busca ciudades 🏰 del End para obtener Elytras y Shulkers.\n"
    "Buena suerte en tu aventura, ¡y que la fuerza de los bloques te acompañe! 🏰✨\n\n")


@bot.command(help="Información sobre los minerales")
async def minerales(ctx):
    mensaje = ""
    for mineral, info in data["minerales"].items():
        mensaje += f"🪨 **{mineral.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n"
        mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
        mensaje += f"⭐ Rareza: {info['rareza']}\n\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre los diamantes")
async def diamantes(ctx):
    info = data["minerales"]["diamantes"] # accedes directo a los datos de diamantes
    mensaje = f"🪨 **Diamantes**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre las esmeraldas")
async def esmeraldas(ctx):
    info = data["minerales"]["esmeraldas"] # accedes directo a los datos de esmeraldas
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre el oro")
async def oro(ctx):
    info = data["minerales"]["oro"] # accedes directo a los datos de oro
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre el redstone")
async def redstone(ctx):
    info = data["minerales"]["redstone"] # accedes directo a los datos de redstone
    mensaje = f"🪨 **redstone**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(name = "carbon", help="informacion sobre el carbón" )  # sin tilde aquí
async def carbon(ctx):
    info = data["minerales"]["carbón"] # accedes directo a los datos de carbon
    mensaje = f"🪨 **carbón**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre el hierro")
async def hierro(ctx):
    info = data["minerales"]["hierro"] # accedes directo a los datos de hierro
    mensaje = f"🪨 **hierro**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"

    await ctx.send(mensaje)

@bot.command(name="lapislazuli", help="informacion sobre la lapislázuli")  # sin tilde aquí
async def lapislazuli_cmd(ctx):
    info = data["minerales"]["lapislázuli"]  # sí con tilde aquí, porque es la clave en JSON
    mensaje = f"🪨 **Lapislázuli**\n"
    mensaje += f"📜 Descripción: {info['descripcion']}\n"
    mensaje += f"⬇️ Mejor altura: {info['mejor_altura']}\n"
    mensaje += f"⭐ Rareza: {info['rareza']}\n"
    
    await ctx.send(mensaje)

@bot.command(help="Información sobre los mundos de Minecraft")
async def mundos(ctx):
    mensaje = ""
    for mundo, info in data["mundos"].items():
        mensaje += f"🌍 **{mundo.capitalize()}**\n\n"
    await ctx.send(mensaje)

@bot.command(help="Información sobre los biomas del Overworld")
async def biomas(ctx):
    mensaje = ""
    for biomas, info in data["mundos"]["overworld"]["biomas"].items():
        mensaje += f"🌱 **{biomas.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n\n"

    await ctx.send(mensaje)  # Envía cada parte por separado

@bot.command(help="Información sobre los biomas del Nether")
async def biomas_nether(ctx):
    mensaje = ""
    for biomas, info in data["mundos"]["nether"]["biomas"].items():
        mensaje += f"🌱 **{biomas.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n\n"

    await ctx.send(mensaje)  # Envía cada parte por separado

@bot.command(help="Información sobre los biomas del End")
async def biomas_end(ctx):
    mensaje = ""
    for biomas, info in data["mundos"]["end"]["biomas"].items():
        mensaje += f"🌱 **{biomas.capitalize()}**\n"
        mensaje += f"📜 Descripción: {info['descripcion']}\n\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre los mobs del Overworld")
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

@bot.command(help="Información sobre los mobs del Nether")
async def mobs_nether(ctx):
    mensaje = ""
    nether_mobs = data["mundos"]["nether"]["mobs"]
    
    for tipo, mobs in nether_mobs.items():  # tipo será "hostil" o "pasivos"
        mensaje += f"🐶 **{tipo.capitalize()}**:\n"
        for mob, info in mobs.items():
            mensaje += f"🐾 **{mob.capitalize()}**\n"
            mensaje += f"📜 Descripción: {info['descripcion']}\n"
            mensaje += f"💔 Vida: {info['vida']}\n"
            mensaje += f"⚔️ Daño: {info['daño']}\n\n"

    await ctx.send(mensaje)

@bot.command(help="Información sobre los mobs del End")
async def mobs_end(ctx):
    mensaje = ""
    end_mobs = data["mundos"]["end"]["mobs"]
    
    for tipo, mobs in end_mobs.items():
        mensaje += f"🐶 **{tipo.capitalize()}**:\n"
        for mob, info in mobs.items():
            if not isinstance(info, dict) or 'vida' not in info or 'daño' not in info:
                continue

            mensaje += f"🐾 **{mob.capitalize()}**\n"
            mensaje += f"📜 Descripción: {info['descripcion']}\n"
            mensaje += f"💔 Vida: {info['vida']}\n"
            mensaje += f"⚔️ Daño: {info['daño']}\n\n"

    await ctx.send(mensaje)
    


TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)