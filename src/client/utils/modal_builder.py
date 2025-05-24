import discord 
import logging
from typing import Union, List, Coroutine

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
            if not style in self.text_styles.keys():
                logging.error(f"[⚠] O estilo {style} não existe! Os estilos disponíveis para InputTexts são: [short, long, paragraph]")
            else:
                style = self.text_styles[style.lower()]
            
        super().__init__(
            label=label,
            style=style,
            placeholder=placeholder,
            custom_id=custom_id, 
            required=required if required else True
        )
        
class ModalBuilder(discord.ui.Modal):
    def __init__(self, title: str=None, custom_id: str=None, persistent: bool=None, *, items: Union[List[InputTextBuilder], InputTextBuilder]=None, modal_listener: Coroutine):
        self.modal_listener = modal_listener
        
        if items is None:
            raise TypeError("Erro: Nenhum item foi passado!")
            
        super().__init__(
            title=title,
            timeout=None if persistent else 180,
            custom_id=custom_id
        )
        
        if isinstance(items, list):
            if len(items) > 5:
                logging.error("[⚠] As modais podem ter no máximo 5 itens!")
                items = items[:5]
                
            for item in items:
                self.add_item(item)
        else:
            self.add_item(items)
    
    async def on_submit(self, interaction: discord.Interaction):
        if not self.modal_listener:
            logging.error("[⚠] Você não passou nenhuma função para o paramêtro 'modal_listener'!")
            return 
        
        await self.modal_listener(interaction)