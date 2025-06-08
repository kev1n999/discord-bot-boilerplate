import discord 
from core.builders.select_builder import (
    SelectMenuBuilder, 
    SelectOptionBuilder, 
    SelectUserBuilder, 
    SelectChannelBuilder,
    SelectRoleBuilder
)
from core.builders.component_builder import ComponentBuilder

async def returns_user_avatar(interaction: discord.Interaction, select: discord.ui.Select) -> None:
    user = select.values[0]
    avatar = user.display_avatar 
    embed = discord.Embed(
        title=f"🖼 Avatar from {user.name}",
        color=discord.Colour.blue() 
    )
    embed.set_image(url=avatar.url)

    await interaction.response.edit_message(
        embed=embed
    )

selected_user = ComponentBuilder(SelectUserBuilder(
    placeholder="Select a user...",
    custom_id="sel-user",
    select_listener=returns_user_avatar
))