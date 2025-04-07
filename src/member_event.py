import discord


async def on_member_join(
    member: discord.Member,
    join_channel_id: int,
):
    """
    Sends an embed message when a new member joins the server.

    Args:
        member: The discord.Member object representing the member who joined.
        join_channel_id: The ID of the channel to send the welcome message to.
    """
    # Validate the channel ID
    if not isinstance(join_channel_id, int) or join_channel_id <= 0:
        print(f"Invalid join channel ID: {join_channel_id}")
        return

    # Get the channel object from the ID
    channel = member.guild.get_channel(join_channel_id)
    if channel is not None:
        try:
            # Create an Embed object
            embed = discord.Embed(
                description=f"{member.mention} has joined the server.",
                color=discord.Color.green(),  # Green color for join event
            )
            # Add member details to the embed
            embed.add_field(
                name="Username",
                value=f"`{member.name}`",
                inline=True,
            )
            embed.add_field(
                name="User ID",
                value=f"`{member.id}`",
                inline=True,
            )
            # Set the member's avatar as the thumbnail
            if member.avatar:
                embed.set_thumbnail(url=member.avatar.url)
            # Send the embed message to the channel
            await channel.send(embed=embed)
        except discord.Forbidden:
            print(
                f"Cannot send message to the join channel: {join_channel_id}. Check permissions."
            )
        except discord.HTTPException as e:
            print(f"HTTP exception when sending welcome message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in on_member_join: {e}")
    else:
        # Log an error if the channel cannot be found
        print(f"Could not find the join channel with ID: {join_channel_id}")


async def on_member_remove(
    member: discord.Member,
    leave_channel_id: int,
):
    """
    Sends an embed message when a member leaves the server.

    Args:
        member: The discord.Member object representing the member who left.
        leave_channel_id: The ID of the channel to send the leave message to.
    """
    # Validate the channel ID
    if not isinstance(leave_channel_id, int) or leave_channel_id <= 0:
        print(f"Invalid leave channel ID: {leave_channel_id}")
        return

    # Get the channel object from the ID
    channel = member.guild.get_channel(leave_channel_id)
    if channel is not None:
        try:
            # Create an Embed object
            embed = discord.Embed(
                description=f"{member.mention} has left the server.",
                color=discord.Color.red(),  # Red color for leave event
            )
            # Add member details to the embed
            embed.add_field(
                name="Username",
                value=f"`{member.name}`",
                inline=True,
            )
            embed.add_field(
                name="User ID",
                value=f"`{member.id}`",
                inline=True,
            )
            # Set the member's avatar as the thumbnail (if available)
            if member.avatar:
                embed.set_thumbnail(url=member.avatar.url)
            # Send the embed message to the channel
            await channel.send(embed=embed)
        except discord.Forbidden:
            print(
                f"Cannot send message to the leave channel: {leave_channel_id}. Check permissions."
            )
        except discord.HTTPException as e:
            print(f"HTTP exception when sending leave message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in on_member_remove: {e}")
    else:
        # Log an error if the channel cannot be found
        print(f"Could not find the leave channel with ID: {leave_channel_id}")


# Note: Ensure your bot has 'Send Messages' and 'Embed Links' permissions
# in the specified channels (join_channel_id and leave_channel_id).
# You also need to pass these channel IDs to the functions when calling them in your bot's events.
