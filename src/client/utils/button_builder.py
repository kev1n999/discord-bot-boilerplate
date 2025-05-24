import discord 
from typing import Coroutine 

class ButtonBuilder(discord.ui.Button):
    def __init__(self, label: str=None, color: str | discord.ButtonStyle=None, custom_id: str=None, *, button_listener: Coroutine):
        self.button_listener = button_listener
        
        if label is None:
            raise TypeError("Você não passou nenhuma label para o botão!")
        if color is None:
            color = discord.ButtonStyle.secondary
        
        super().__init__(
            label=label,
            style=color,
            custom_id=custom_id
        )
        
    async def callback(self, interaction):
        await self.button_listener(interaction)