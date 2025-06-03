import logging 
from importlib import import_module 
from pathlib import Path 
from src.core.builders.command_builder import SlashCommandBuilder
from discord.app_commands import CommandTree

def load_commands(tree: CommandTree):
    root = Path("src/app/commands")

    for folder_path in root.iterdir():
        if not folder_path.is_dir():
            continue 

        for file_path in folder_path.glob("*.py"):
            if file_path.name == "__init__.py":
                continue

            module_name = f"src.app.commands.{folder_path.name}.{file_path.stem}"

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
                        obj(tree) 
                    except Exception as err:
                        logging.exception(f"Falha ao registrar {obj.__name__}: {err}")