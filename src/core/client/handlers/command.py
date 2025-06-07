from importlib import import_module 
from pathlib import Path 
from core.builders.command_builder import SlashCommandBuilder
from discord.app_commands import CommandTree
from core.utils.logger import setup_logger

# Configura o logger para este módulo
logger = setup_logger(__name__)

def load_commands(tree: CommandTree):
    """
    Carrega todos os comandos registrados nas subpastas de app/commands.
    
    Args:
        tree (CommandTree): Árvore de comandos do Discord onde os comandos serão registrados.
    """
    root = Path("app/commands")
    logger.info("Iniciando carregamento de comandos...")

    for folder_path in root.iterdir():
        if not folder_path.is_dir():
            continue 

        logger.debug(f"Explorando pasta: {folder_path.name}")
        for file_path in folder_path.glob("*.py"):
            if file_path.name == "__init__.py":
                continue

            module_name = f"app.commands.{folder_path.name}.{file_path.stem}"
            logger.debug(f"Tentando importar módulo: {module_name}")

            try:
                module = import_module(module_name)
            except Exception as err:
                logger.error(f"Falha ao importar {module_name}: {err}", exc_info=True)
                continue  

            for obj in module.__dict__.values():
                if (
                    isinstance(obj, type)
                    and issubclass(obj, SlashCommandBuilder)
                    and obj is not SlashCommandBuilder
                ):
                    try:
                        obj(tree)
                        logger.info(f"Comando registrado com sucesso: {obj.__name__}")
                    except Exception as err:
                        logger.error(f"Falha ao registrar {obj.__name__}: {err}", exc_info=True)

    logger.info("Carregamento de comandos concluído")