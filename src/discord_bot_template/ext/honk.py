import arc
from hikari import GuildMessageCreateEvent

plugin = arc.GatewayPlugin(__name__)


# When a human user sends a message in a guild which mentions the bot,
# - reply with "*honking*" if the message contains a carrot emoji,
# - else react with :rabbit2:
@plugin.listen()
async def on_guild_message_create(event: GuildMessageCreateEvent) -> None:
    if not event.is_human:
        return

    if (
        (me := plugin.client.cache.get_me())
        and (user_mentions_ids := event.message.user_mentions_ids)
        and me.id in user_mentions_ids
    ):
        if (content := event.message.content) and "\N{CARROT}" in content:
            _ = await event.message.respond(
                "*honking*", reply=True, mentions_reply=True
            )
            return
        await event.message.add_reaction("\N{RABBIT}")


@arc.loader
def loader(client: arc.GatewayClient) -> None:
    _ = client.add_plugin(plugin)


@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    _ = client.remove_plugin(plugin)
