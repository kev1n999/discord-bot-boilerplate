import os 
import discord 
import logging 
from discord import app_commands 
from dotenv import load_dotenv 
from src.base.builders.command_builder import SlashCommandBuilder 
from pathlib import Path 
from importlib import import_module

load_dotenv()

# Classe para se conectar ao client
class DiscordClient(discord.Client): 
    """
    Cliente principal do bot  que gerencia a conexão, sincronização de comandos e carregamento automático.

    Essa classe estende `discord.Client` e configura um `app_commands.CommandTree` para lidar com comandos de barra (slash commands),
    buscando automaticamente comandos em subpastas de `src/commands/`.

    Args:
        token (str): Token do bot.
        intents (discord.Intents, optional): Intenções do gateway do Discord. Padrão é `discord.Intents.all()`(Todas as intents ativadas).

    Attributes:
        token (str): Token do bot.
        client_intents (discord.Intents): Intents configuradas.
        tree (app_commands.CommandTree): Árvore de comandos usada para registrar e sincronizar os comandos de barra.
    """
    def __init__(self, token, intents=None): 
        self.token = token 
        self.client_intents = intents  
        
        if self.client_intents is None:
            self.client_intents = discord.Intents.all() 
            
        super().__init__(intents=self.client_intents)
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        self.load_commands()
        await self.tree.sync()
        
    def run_bot(self):
        self.run(self.token)
    
    def load_commands(self):
        root = Path("src/discord/commands")

        for folder_path in root.iterdir():
            if not folder_path.is_dir():
                continue 

            for file_path in folder_path.glob("*.py"):
                if file_path.name == "__init__.py":
                    continue

                module_name = f"src.discord.commands.{folder_path.name}.{file_path.stem}"

                try:
                    module = import_module(module_name)
                except Exception as err:
                    logging.exception(f"Falha ao importar {module_name}: {err}")
                    continue  

                for obj in module.__dict__.values():
                    if (
                        isinstance(obj, type)
                        and issubclass(obj, SlashCommandBuilder)
                        and obj is not SlashCommandBuilder
                    ):
                        try:
                            obj(self.tree) 
                        except Exception as err:
                            logging.exception(f"Falha ao registrar {obj.__name__}: {err}")
            
# Cria a instância do bot
client = DiscordClient(token=os.getenv("BOT_TOKEN"))