import os 
import logging
import discord 
from discord import app_commands 

class SlashCommandBuilder(app_commands.Command):
    def __init__(self, app: app_commands.CommandTree, *, name: str=None, description:str=None, callback: callable=None):
        self.app = app 
        
        if name is None:
            print("Err: name command is not defined!")
        
        if callback is None:
            print("Err: command callback is not defined!")
            
        super().__init__(
            name=name,
            description=description,
            callback=callback
        )
        
        try:
            self.app.add_command(self)
        except Exception as err:
            logging.exception(f"Err: {err}")