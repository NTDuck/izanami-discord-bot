
# not to be confused with utils/

from discord.ext.commands import Bot, Cog, Context, command


class UtilityCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    # should require administrative privileges
    @command()
    async def clear(self, ctx: Context, limit: int|str):
        if isinstance(limit, int) and limit > 0:
            limit += + 1
        elif limit == "*":
            limit = None
        else:
            await ctx.send(f"error: param `limit` must be a positive integer or `*`.")
            return
        for perm in ["manage_messages", "read_message_history"]:
            if not getattr(ctx.bot_permissions, perm):
                await ctx.send(f"""
error: bot does not have `{perm}` permissions.
for authenticated users, this can be troubleshooted as follows:
- try re-inviting the bot with said permission enabled.
- try enabling the bot's said permission server-wide and channel-wide.
                """)
                return
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send(f"action failed: invoker `{ctx.author}` does not have `manage_messages` permissions.")
            return
        await ctx.channel.delete_messages(
            messages=[msg async for msg in ctx.channel.history(limit=limit)],
            reason=f"command invoked by `{ctx.author}`.",
        )
        if limit is None:
            limit = "all"
        await ctx.channel.send(
            content=f"action complete: deleted `{limit}` messages in channel `{ctx.channel}`.",
            delete_after=float(1),
        )