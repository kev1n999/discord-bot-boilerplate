import discord 
from typing import List 

class InputTextBuilder(discord.ui.TextInput):
    def __init__(self, label: str=None, style:str | discord.TextStyle=None, custom_id: str | None=None):
        if label is None:
            raise TypeError("Erro: Label não informado na criação do InputText!")
        
        if style is None:
            style = discord.TextStyle.short
            
        super().__init__(
            label=label,
            style=style,
            custom_id=custom_id
        )
        
class ModalBuilder(discord.ui.Modal):
    def __init__(self, title: str=None, custom_id: str=None, persistent: bool=None, *, items: List[InputTextBuilder] | discord.TextInput=None):
        if items is None:
            raise TypeError("Erro: Nenhum item foi passado!")
        
        super().__init__(
            title=title,
            timeout=None if persistent else 180,
            custom_id=custom_id
        )
        
        if isinstance(items, list):
            for item in items:
                self.add_item(item)
        else:
            self.add_item(items)

