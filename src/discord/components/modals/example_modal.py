import discord 
from src.base.builders.component_builder import ComponentBuilder
from src.base.builders.modal_builder import ModalBuilder, InputTextBuilder

modal_fields = [
    InputTextBuilder(label="Number", placeholder="Type a number!", required=True, custom_id="sum1"),
    InputTextBuilder(label="Other number", placeholder="Type another number!", required=True, custom_id="sum2")
]

async def modal_listener(interaction: discord.Interaction):
    number1 = int(modal_fields[0].value)
    number2 = int(modal_fields[1].value)
    
    await interaction.response.send_message(
        content=f"The sum is: {number1 + number2}",
        ephemeral=True
    )
    
modalSum = ModalBuilder(title="Sum the two numbers", items=modal_fields, modal_listener=modal_listener, custom_id="modal example")