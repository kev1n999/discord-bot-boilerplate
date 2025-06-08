import discord 
from typing import List, Union

class ComponentBuilder(discord.ui.View):
    """
    Builder para criar um `discord.ui.View` com componentes interativos como botões ou menus.

    Essa classe permite adicionar um único componente ou uma lista de componentes (exceto modais e text inputs, que são tratados separadamente).

    Args:
        component (Union[List[discord.Component], discord.Component]):
            Um ou mais componentes (como `discord.ui.Button`, `discord.ui.Select`, etc.) a serem adicionados à view.
        persistent (bool, optional):
            Se `True`, a view não expira (timeout = None). Caso contrário, expira em 180 segundos. Padrão é `False`.

    Raises:
        TypeError: Se nenhum componente for passado.
        TypeError: Se um componente inválido for incluído (ex: `discord.ui.Modal` ou `discord.ui.TextInput`).

    Exemplo:
        button = discord.ui.Button(label="Clique aqui", style=discord.ButtonStyle.primary)
        view = ComponentBuilder(component=button)

        await interaction.response.send_message("Clique no botão!", view=view)
    """
    
    def __init__(
        self, 
        component: Union[List[discord.Component], discord.Component], 
        persistent: bool=None
    ) -> None:
        super().__init__(timeout=None if persistent else 180)
        
        if component is None:
            raise TypeError("Nenhum componente(Button, SelectMenu, Modal) foi passado!")
        
        if isinstance(component, list):
            for c in component:
                if isinstance(c, discord.Component):
                    raise TypeError(f"Erro: Não é possível adicionar uma lista de componentes do tipo {type(c)}!")
                self.add_item(c)
        else:
            self.add_item(component)