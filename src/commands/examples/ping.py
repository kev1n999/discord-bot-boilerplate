import discord 
from src.base.client.utils.command_builder import SlashCommandBuilder
from src.base.client.utils.select_builder import SelectMenuBuilder, SelectOptionBuilder
from src.base.client.utils.component_builder import ComponentBuilder

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
        select = SelectMenuBuilder(placeholder="selecione alguma opc", options=options, select_listener=self.select_listener)
        
        await interaction.response.send_message(view=ComponentBuilder(select))
    
    async def select_listener(self, interaction: discord.Interaction, select: discord.ui.Select):
        if select.values[0] == "a":
            await interaction.response.send_message(ephemeral=True, content="Você selecionou a opção a meu mano!")