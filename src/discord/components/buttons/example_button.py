import discord 
from src.base.builders.button_builder import ButtonBuilder
from src.base.builders.component_builder import ComponentBuilder



async def button_listener(interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(
        content="Hello!",
        ephemeral=True 
    )
    
button = ButtonBuilder(
    label="button example",
    color="green",
    button_listener=button_listener 
)

buttonComponent = ComponentBuilder(button)