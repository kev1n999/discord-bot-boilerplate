import discord 
from typing import List, Coroutine

class InputTextBuilder(discord.ui.TextInput):
    def __init__(self, label: str=None, placeholder: str=None, style:str | discord.TextStyle=None, custom_id: str | None=None, required: bool=None):
        self.text_styles = {
            "short": discord.TextStyle.short ,
            "long": discord.TextStyle.long,
            "paragraph": discord.TextStyle.paragraph
        }
        
        if label is None:
            raise TypeError("Erro: Label não informado na criação do InputText!")
        
        if style is None:
            style = self.text_styles["short"]
        else:
            style = self.text_styles[style.lower()]
        
        if required is None:
            required = True 
            
        super().__init__(
            label=label,
            style=style,
            placeholder=placeholder,
            custom_id=custom_id, 
            required=required
        )
        
class ModalBuilder(discord.ui.Modal):
    def __init__(self, title: str=None, custom_id: str=None, persistent: bool=None, *, items: List[InputTextBuilder] | discord.TextInput=None, modal_listener: Coroutine):
        self.modal_listener = modal_listener
        
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
    
    async def on_submit(self, interaction: discord.Interaction):
        await self.modal_listener(interaction)