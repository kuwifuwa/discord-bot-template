import tomllib

import arc
import hikari
from hikari import Intents


def main() -> None:
    # Store the Discord Bot Token in secrets/discord.toml
    with open("secrets/discord.toml", "rb") as f:
        token = tomllib.load(f)["token"]

    bot = hikari.GatewayBot(
        token=token,
        intents=(Intents.ALL_UNPRIVILEGED),
    )
    client = arc.GatewayClient(bot)

    # Organize features into extensions via hikari-arc
    _ = client.load_extension("discord_bot_template.ext.honk")

    bot.run()
