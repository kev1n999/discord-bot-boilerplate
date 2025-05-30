import discord 
from src.base.builders.command_builder import SlashCommandBuilder
from src.discord.components.buttons.example_button import buttonComponent

class ButtonExample(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="button",
            description="Envia um botão de exemplo!"
        )
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=buttonComponent)