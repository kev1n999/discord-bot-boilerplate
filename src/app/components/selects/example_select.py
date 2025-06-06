import discord 
from core.builders.select_builder import (
    SelectMenuBuilder, 
    SelectOptionBuilder, 
    SelectUserBuilder, 
    SelectChannelBuilder,
    SelectRoleBuilder
)
from core.builders.component_builder import ComponentBuilder

select_options = [
    SelectOptionBuilder(label="option 1", description="this is option 1", value="option 1"),
    SelectOptionBuilder(label="option 2", description="this is option 2", value="option 2"),
    SelectOptionBuilder(label="option 3", description="This is option 3", value="option 3")
]

async def select_listener(interaction: discord.Interaction, select: discord.ui.Select):
    if select.values[0] == "option 1":
        await interaction.response.send_message("You have selected option 1")
    elif select.values[0] == "option 2":
        await interaction.response.send_message("You have selected option 2")
    elif select.values[0] == "option 3":
        await interaction.response.send_message("You have selected option 3")
        
select_menu = SelectMenuBuilder(
    placeholder="Select one option", 
    options=select_options, 
    select_listener=select_listener)

select_component = ComponentBuilder(select_menu)

async def selected_user(interaction: discord.Interaction, select: discord.ui.UserSelect):
    user = select.values[0]
    await interaction.response.send_message("Selected user: " + user.name)
    
select_user = ComponentBuilder(SelectUserBuilder(
    placeholder="Selecione um usuário",
    select_listener=selected_user,
    custom_id="slk"
))