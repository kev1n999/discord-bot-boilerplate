import discord 
from typing import List 

class ComponentBuilder(discord.ui.View):
    def __init__(self, component: List[discord.Component] | discord.Component=None, persistent: bool=False):
        super().__init__(timeout=None if persistent is True else 180)
        
        if component is None:
            raise TypeError("Nenhum componente(Button, SelectMenu, Modal) foi passado!")
        
        if isinstance(component, list):
            for c in component:
                self.add_item(c)
        else:
            self.add_item(component)