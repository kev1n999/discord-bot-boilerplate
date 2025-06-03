import os 
import discord 
from discord import app_commands 
from dotenv import load_dotenv 
from src.core.builders.command_builder import SlashCommandBuilder
from src.core.handlers.command import load_commands

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
        load_commands(self.tree)
        await self.tree.sync()
        
    def run_bot(self):
        self.run(self.token)
            
# Cria a instância do bot
client = DiscordClient(token=os.getenv("BOT_TOKEN"))