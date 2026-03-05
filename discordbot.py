# bot.py
import os
import discord # type: ignore
from discord.ext import commands # type: ignore
from threading import Thread
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# ---- Keep-alive web server (utile pour certains hebergeurs/pings) ----
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Bot Discord en ligne.")

    def log_message(self, format, *args):
        # Silence default HTTP logs
        return


def run_web():
    port = int(os.getenv("PORT", 8080))
    server = ThreadingHTTPServer(("0.0.0.0", port), KeepAliveHandler)
    server.serve_forever()


def keep_alive():
    t = Thread(target=run_web, daemon=True)
    t.start()


def _read_token_from_env_path(env_path):
    if not os.path.exists(env_path):
        return None

    with open(env_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == "DISCORD_TOKEN":
                token = value.strip().strip("\"'")
                if token:
                    return token
    return None


def load_token_from_env_file():
    for env_path in (".env", ".venv/.env"):
        token = _read_token_from_env_path(env_path)
        if token:
            return token
    return None


def normalize_and_validate_token(token):
    if not token:
        return None

    token = token.strip().strip("\"'")
    if token.lower().startswith("bot "):
        token = token[4:].strip()

    if token == "DISCORD_TOKEN" or token == "COLLE_TON_VRAI_BOT_TOKEN" or not token:
        return None

    return token


# ---- Bot Discord ----
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Connecte en tant que {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


if __name__ == "__main__":
    keep_alive()
    token = "DISCORD_TOKEN"  # Valeur par défaut pour éviter les erreurs si aucune variable d'environnement n'est trouvée
    token = load_token_from_env_file() or os.getenv("DISCORD_TOKEN", token)
    token = normalize_and_validate_token(token)
    if not token:
        raise ValueError(
            "Token invalide. Mets le vrai Bot Token Discord directement dans video.py"
        )
    bot.run(token)
