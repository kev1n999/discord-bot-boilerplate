import discord 
from src.client.utils.command_builder import SlashCommandBuilder

# Simple example for creating commands for the bot
class ExampleCommandPing(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree, # Default
            name="ping", # Command name
            description="Reply with pong!", # Command description
            callback=self.command_callback # Command callback
        )
        
    # Command callback
    async def command_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="Pong!")