import logging 
import discord 
from typing import Union, List, Coroutine

class SelectOptionBuilder(discord.SelectOption):
    def __init__(self, label: str=None, description: str=None, value: str=None, emoji: discord.PartialEmoji=None):
        super().__init__(
            label=label,
            description=description,
            value=value,
            emoji=emoji
        )
        
class SelectMenuBuilder(discord.ui.Select):
    def __init__(self, placeholder: str=None, options: Union[List[SelectOptionBuilder], SelectOptionBuilder]=None):
        super().__init__(
            placeholder=placeholder,
            options=options
        )
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("a")