import discord 
from src.core.builders.command_builder import SlashCommandBuilder

# Simple example for creating commands for the bot
class ExampleCommandPing(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree, # Padrão
            name="ping", # Nome do comando
            description="Reply with pong!", # Descrição do comando
        )
        
    # Responde ao comando
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content="Pong!",
            ephemeral=True
        )