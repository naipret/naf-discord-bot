import discord


async def on_member_join(
    member: discord.Member,
    join_channel_id: int,
):
    # Validate the channel ID
    if not isinstance(join_channel_id, int) or join_channel_id <= 0:
        print("Invalid join channel ID:", join_channel_id)
        return

    # Get the channel where the welcome message will be sent
    channel = member.guild.get_channel(join_channel_id)
    if channel is not None:
        try:
            # Send a message to the channel when a member joins
            await channel.send(
                f"{member.mention} | `{member.name}` | `{member.id}` has joined the server!"
            )
        except discord.Forbidden:
            print(
                f"Cannot send message to the join channel: {join_channel_id}. Check permissions."
            )
    else:
        # Log an error if the channel cannot be found
        print(f"Could not find the join channel with ID:", join_channel_id)


async def on_member_remove(
    member: discord.Member,
    leave_channel_id: int,
):
    # Validate the channel ID
    if not isinstance(leave_channel_id, int) or leave_channel_id <= 0:
        print("Invalid leave channel ID:", leave_channel_id)
        return

    # Get the channel where the leave message will be sent
    channel = member.guild.get_channel(leave_channel_id)
    if channel is not None:
        try:
            # Send a message to the channel when a member leaves
            await channel.send(
                f"{member.mention} | `{member.name}` | `{member.id}` has left the server!"
            )
        except discord.Forbidden:
            print(
                f"Cannot send message to the leave channel: {leave_channel_id}. Check permissions."
            )
    else:
        # Log an error if the channel cannot be found
        print(f"Could not find the leave channel with ID: {leave_channel_id}")


# Note: Ensure your bot has 'Send Messages' and 'Embed Links' permissions
# in the specified channels (join_channel_id and leave_channel_id).
# You also need to pass these channel IDs to the functions when calling them in your bot's events.
