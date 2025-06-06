import discord 
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder

label_number = 0
label_string = str(label_number)
        
async def button_listener(interaction: discord.Interaction, button: discord.ui.Button):
    button.label = str(label_string)
    await interaction.response.edit_message(view=ComponentBuilder(button))
    
button = ButtonBuilder(
    label=label_string,
    color="green",
    button_listener=button_listener 
)

buttonComponent = ComponentBuilder(button)