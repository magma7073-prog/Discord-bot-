# bot.py
import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# ---- Keep-alive web server (utile pour certains hébergeurs/pings) ----
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Discord en ligne."

def run_web():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# ---- Bot Discord ----
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    keep_alive()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN manquant dans les variables d'environnement")
    bot.run(token)
