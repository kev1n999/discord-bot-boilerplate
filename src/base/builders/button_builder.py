import discord 
import logging 
from typing import Coroutine 

class ButtonBuilder(discord.ui.Button):
    """
    Botão personalizado para interações usando um listener assíncrono.

    Herda de:
        discord.ui.Button

    Args:
        label (str): Texto exibido no botão.
        color (str | discord.ButtonStyle): Estilo do botão (primary, secondary, success, etc). Pode ser uma string ou uma constante do Discord.
        custom_id (str): ID único usado para identificar o botão nas interações.
        button_listener (Coroutine): Função assíncrona que será executada quando o botão for clicado.

    Raises:
        TypeError: Se a label não for fornecida.

    Exemplo:
        async def on_click(interaction):
            await interaction.response.send_message("Botão clicado!")

        button = ButtonBuilder(label="Clique aqui", color="primary", button_listener=on_click)
    """
    
    def __init__(self, label: str=None, color: str | discord.ButtonStyle=None, custom_id: str=None, *, button_listener: Coroutine):
        self.button_listener = button_listener
        self.colors = {
            "blurple": discord.ButtonStyle.blurple,
            "green": discord.ButtonStyle.green,
            "red": discord.ButtonStyle.danger,
            "primary": discord.ButtonStyle.primary,
            "secondary": discord.ButtonStyle.secondary
        }
        
        if label is None:
            raise TypeError("Você não passou nenhuma label para o botão!")
        if color is None:
            color = self.colors["secondary"]
            
        else:
            if isinstance(color, str):
                if not color in self.colors.keys():
                    logging.error(f"[⚠] A cor '{color}' não existe! Use: {list(self.colors.keys())}")
                    color = self.colors["secondary"]
                else:
                    color = self.colors[color.lower()]
        
        super().__init__(
            label=label,
            style=color,
            custom_id=custom_id
        )
        
    async def callback(self, interaction):
        await self.button_listener(interaction)