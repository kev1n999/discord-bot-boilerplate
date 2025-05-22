from src.client.utils.command_builder import SlashCommandBuilder  
from discord import User 

class AvatarExampleCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="avatar",
            description="retorna o avatar do usuário mencionado",
            callback=self.callback 
        )
        
    # Você pode adicionar paramêtros/opções ao comando dessa forma
    async def callback(self, interaction, user:User):
        await interaction.response.send_message(user.display_avatar)