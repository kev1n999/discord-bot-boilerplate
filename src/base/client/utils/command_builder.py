import logging
from discord import app_commands 

# Classe para a criação de novos comandos
class SlashCommandBuilder(app_commands.Command):
    def __init__(self, app: app_commands.CommandTree, *, name: str=None, description:str=None):
        self.app = app 
        
        callback = getattr(self, "callback", None)
        
        if not callable(callback):
            raise NotImplementedError("Erro: Você deve implementar um método callback(async def callback(self, interaction))...")
        
        super().__init__(
            name=name,
            description=description,
            callback=callback
        )
        
        try:
            self.app.add_command(self)
        except Exception as err:
            logging.exception(f"Err: {err}")