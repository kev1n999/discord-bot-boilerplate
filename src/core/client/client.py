import os 
import discord 
from discord import app_commands 
from dotenv import load_dotenv 
from core.builders.command_builder import SlashCommandBuilder
from handlers.command import load_commands
from core.utils.logger import setup_logger

load_dotenv()

# Configura o logger para este módulo
logger = setup_logger(__name__)

# Classe para se conectar ao client
class DiscordClient(discord.Client): 
    """
    Cliente principal do bot que gerencia a conexão, sincronização de comandos e carregamento automático.

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
            logger.debug("Usando todas as intents do Discord")
            
        super().__init__(intents=self.client_intents)
        self.tree = app_commands.CommandTree(self)
        logger.info("Cliente Discord inicializado")
        
    async def setup_hook(self):
        logger.info("Configurando hooks do bot...")
        load_commands(self.tree)
        await self.tree.sync()
        logger.info("Comandos sincronizados com sucesso")
        
    async def on_ready(self):
        logger.info(f"Bot está online como {self.user.name} (ID: {self.user.id})")
        
    async def on_error(self, event_method, *args, **kwargs):
        logger.error(f"Erro no evento {event_method}", exc_info=True)
        
    def run_bot(self):
        try:
            logger.info("Iniciando conexão com o Discord...")
            self.run(self.token)
        except Exception as e:
            logger.error(f"Erro ao conectar com o Discord: {str(e)}", exc_info=True)
            raise
            
# Cria a instância do bot
client = DiscordClient(token=os.getenv("BOT_TOKEN"))