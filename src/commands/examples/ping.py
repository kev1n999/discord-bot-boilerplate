import discord 
from src.client.utils.command_builder import SlashCommandBuilder
from src.client.utils.modal_builder import InputTextBuilder, ModalBuilder

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
        i = InputTextBuilder(label="oi", style="long", placeholder="test placeholder", custom_id="a")
        
        modal = ModalBuilder(title="modal1", items=[i], custom_id="a", modal_listener=self.modal_listener)
        
        await interaction.response.send_modal(modal)
        
    async def modal_listener(self, interaction):
        await interaction.response.send_message("pong")