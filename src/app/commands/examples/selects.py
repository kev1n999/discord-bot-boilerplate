import discord
from core.builders.command_builder import SlashCommandBuilder
from app.components.selects.example_select import * 

class SelectTestCommands(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="select_channel",
            description="Testa selects de canais"
        )
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=select_menu_channel)