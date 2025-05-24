import discord 
from src.client.utils.command_builder import SlashCommandBuilder
from src.client.utils.select_builder import SelectMenuBuilder, SelectOptionBuilder
from src.client.utils.component_builder import ComponentBuilder

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
        options = [
            SelectOptionBuilder(label="oi", description="oi2", value="a"),
            SelectOptionBuilder(label="ola", description="ola2", value="b")
        ]
        select = SelectMenuBuilder(placeholder="selecione alguma opc", options=options)
        
        await interaction.response.send_message(view=ComponentBuilder(select))