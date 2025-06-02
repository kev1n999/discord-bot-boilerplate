import discord 
from src.app.components.buttons.example_button import buttonComponent
from src.core.builders.command_builder import SlashCommandBuilder 

class ButtonExample(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="button",
            description="Envia um botão de exemplo!"
        )
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=buttonComponent)