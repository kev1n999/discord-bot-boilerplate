import discord
from core.builders.command_builder import SlashCommandBuilder
from ...components.selects.example_select import selected_user 

class AvatarUserCOmmand(SlashCommandBuilder):
    def __init__(self, tree) -> None:
        super().__init__(
            app=tree,
            name="avatar",
            description="Returns avatar of the mentioned user"
        )

    async def callback(self, interaction: discord.Interaction, user: discord.User=None) -> None:
        if user is None:
            user = interaction.user 
        
        avatar = user.display_avatar 
        embed = discord.Embed(
            title=f"🖼 Avatar from {user.name}",
            color=discord.Colour.blue() 
        )
        embed.set_image(url=avatar.url)

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True,
            view=selected_user
        )