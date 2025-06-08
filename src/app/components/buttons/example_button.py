import discord 
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder

num = 0

async def counter(interaction: discord.Interaction, button: discord.ui.Button) -> None:
    global num 
    num += 1
    button.label = str(num)
    await interaction.response.edit_message(view=ComponentBuilder(button))

button = ComponentBuilder(ButtonBuilder(
    label=str(num),
    button_listener=counter 
))