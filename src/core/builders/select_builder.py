import discord 
from typing import Union, List, Coroutine

class SelectOptionBuilder(discord.SelectOption):
    """
    Classe auxiliar para criar uma opção de menu seletor.
    
    Herda de: 
        discord.SelectOption
        
    Params:
        label (str): Texto que será exibido na opção.
        description (str): Descrição que será exibida logo abaixo do label na opção.
        value (str): Valor interno da opção (Usado para identificar uma opção específica futuramente);
        emoji (discord.PartialEmoji): Emoji opcional a ser adicionado ao lado do label.
    """
    def __init__(
        self, 
        label: str=None, 
        description: str=None, 
        value: str=None, 
        emoji: discord.PartialEmoji=None
    ):
        super().__init__(
            label=label,
            description=description,
            value=value,
            emoji=emoji
        )
        
        
        
class SelectMenuBuilder(discord.ui.Select):
    """
    Menu seletor (dropdown) personalizado com listener assíncrono para interações.

    Herda de:
        discord.ui.Select

    Args:
        placeholder (str): Texto exibido quando nenhuma opção está selecionada.
        options (Union[List[SelectOptionBuilder], SelectOptionBuilder]): Lista de opções a serem exibidas no menu.
        select_listener (Coroutine): Função assíncrona chamada ao selecionar uma opção.

    Exemplo:
        async def listener(interaction, select):
            await interaction.response.send_message(f"Selecionado: {select.values[0]}")

        select = SelectMenuBuilder(
            placeholder="Escolha uma opção",
            options=[SelectOptionBuilder(label="Opção 1", value="1")],
            select_listener=listener
        )
    """
    def __init__(
        self, 
        placeholder: str=None, 
        options: Union[List[SelectOptionBuilder], SelectOptionBuilder]=None, 
        *, 
        select_listener: Coroutine
    ):
        super().__init__(
            placeholder=placeholder,
            options=options
        )
        self.select_listener = select_listener 
        
    async def callback(self, interaction: discord.Interaction):
        await self.select_listener(interaction, select=self)



class SelectUserBuilder(discord.ui.UserSelect):
    """
    Builder para criar um SelectMenu de seleção de membros (usuários do servidor).

    Herda de:
        discord.ui.UserSelect

    Args:
        placeholder (str): Texto exibido quando nenhuma opção está selecionada.
        custom_id (str): ID personalizado da interação do select.
        select_listener (Coroutine): Função assíncrona chamada ao selecionar um usuário.

    Exemplo:
        async def on_user_selected(interaction, select):
            await interaction.response.send_message(f"Usuário: {select.values[0]}")

        menu = SelectUserBuilder(select_listener=on_user_selected)
    """
    
    def __init__(
        self,
        placeholder: str=None,
        *, 
        custom_id: str=None,
        select_listener: Coroutine
    ):
        super().__init__(
            custom_id=custom_id,
            placeholder=placeholder if placeholder else "Select a member...",
        )
        self.select_listener = select_listener
    
    async def callback(self, interaction):
        await self.select_listener(interaction, select=self)



class SelectRoleBuilder(discord.ui.RoleSelect):
    """
    Builder para criar um SelectMenu de seleção de cargos (roles) do servidor.

    Herda de:
        discord.ui.RoleSelect

    Args:
        placeholder (str): Texto exibido quando nenhuma opção está selecionada.
        custom_id (str): ID personalizado da interação do select.
        select_listener (Coroutine): Função assíncrona chamada ao selecionar um cargo.

    Exemplo:
        async def on_role_selected(interaction, select):
            await interaction.response.send_message(f"Cargo: {select.values[0].name}")

        menu = SelectRoleBuilder(select_listener=on_role_selected)
    """

    def __init__(
        self,
        placeholder: str=None,
        *,
        custom_id: str=None,
        select_listener: Coroutine
    ):
        super().__init__(
            placeholder=placeholder if placeholder else "Select a role...",
            custom_id=custom_id,
        )
        self.select_listener = select_listener
        
    async def callback(self, interaction):
        await self.select_listener(interaction, select=self)


class SelectChannelBuilder(discord.ui.ChannelSelect):
    """
    Builder para criar um SelectMenu de canais do servidor.

    Herda de:
        discord.ui.ChannelSelect

    Args:
        placeholder (str): Texto exibido quando nenhuma opção está selecionada.
        channel_types (List[discord.ChannelType] | str): Lista de tipos de canal aceitos (texto, voz, etc).
        select_listener (Coroutine): Função assíncrona chamada ao selecionar um canal.

    Exemplo:
        async def on_channel_selected(interaction, select):
            await interaction.response.send_message(f"Canal: {select.values[0].mention}")

        menu = SelectChannelBuilder(
            channel_types=[discord.ChannelType.text],
            select_listener=on_channel_selected
        )
    """
    
    def __init__(
        self, 
        placeholder: str=None,
        *,
        channel_types: Union[List[discord.ChannelType], str],
        select_listener: Coroutine
    ):
        super().__init__(
            placeholder=placeholder if placeholder else "Select a channel...",
            channel_types=channel_types,
        )
        self.select_listener = select_listener
        
    async def callback(self, interaction):
        await self.select_listener(interaction, select=self)