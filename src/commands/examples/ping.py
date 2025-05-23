import discord 
from src.client.utils.command_builder import SlashCommandBuilder 
from src.client.utils.button_builder import ButtonBuilder
from src.client.utils.component_builder import ComponentBuilder

class PingCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="ping",
            description="Responde com pong!",
            callback=self.callback 
        )
        
    async def callback(self, interaction: discord.Interaction):
        button = ButtonBuilder(
            label="oi",
        )
        
        newbutton = ButtonBuilder("seloko", color=discord.ButtonStyle.green)
        
        component = ComponentBuilder([button, newbutton])
        await interaction.response.send_message(view=component)