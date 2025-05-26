import discord 
from src.base.builders.command_builder import SlashCommandBuilder
from src.base.builders.select_builder import SelectMenuBuilder, SelectOptionBuilder
from src.discord.components.modals.example_modal import modalSum

# Simple example for creating commands for the bot
class ExampleCommandPing(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree, # Default
            name="ping", # Command name
            description="Reply with pong!", # Command description
        )
        
    # Command callback
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(modalSum)