import discord 
from core.builders.command_builder import SlashCommandBuilder
from ...components.buttons.example_button import button 

class PingCommand(SlashCommandBuilder):
    def __init__(self, tree) -> None:
        super().__init__(
            app=tree,
            name="ping",
            description="Reply with pong!",
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content="Pong!",
            ephemeral=True,
            view=button
        )