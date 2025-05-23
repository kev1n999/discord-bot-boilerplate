import discord 

class ButtonParams:
    def __init__(self, label: str=None, color: str | discord.ButtonStyle=None, custom_id: str=None, persistent: bool=None):
        self.ButtonLabel = label 
        self.ButtonColor = color 
        self.ButtonCustomId = custom_id
        self.persistent = persistent

class ButtonBuilder(discord.ui.Button):
    def __init__(self, label: str=None, color: str | discord.ButtonStyle=None, custom_id: str=None):
        if label is None:
            raise TypeError("Você não passou nenhuma label para o botão!")
        if color is None:
            color = discord.ButtonStyle.secondary
        
        super().__init__(
            label=label,
            style=color,
            custom_id=custom_id
        )