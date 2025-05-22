from src.client.utils.command_builder import SlashCommandBuilder 

class PingCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="ping",
            description="Responde com pong!",
            callback=self.callback 
        )
        
    async def callback(self, interaction):
        await interaction.response.send_message("pong!")