import discord 
from typing import List, Union

class ComponentBuilder(discord.ui.View):
    def __init__(self, component: Union[List[discord.Component], discord.Component], persistent: bool=None):
        super().__init__(timeout=None if persistent else 180)
        
        if component is None:
            raise TypeError("Nenhum componente(Button, SelectMenu, Modal) foi passado!")
        
        if isinstance(component, list):
            for c in component:
                if isinstance(c, discord.ui.Modal) or isinstance(c, discord.ui.Select) or isinstance(c, discord.ui.TextInput):
                    raise TypeError(f"Erro: Não é possível adicionar uma lista de componentes do tipo {type(c)}!")
                self.add_item(c)
        else:
            self.add_item(component)