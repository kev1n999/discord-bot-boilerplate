import discord 
from discord import app_commands 

class DiscordClient(discord.Client):
    def __init__(self, token, intents=None):
        self.token = token
        self.client_intents = intents 
        
        if self.client_intents is None:
            self.client_intents = discord.Intents.all()
            
        super().__init__(intents=self.client_intents)
        self.tree = app_commands.CommandTree(self)
        
    async def on_ready(self):
        print("Bot online!")
        
    def run_bot(self):
        self.run(self.token)