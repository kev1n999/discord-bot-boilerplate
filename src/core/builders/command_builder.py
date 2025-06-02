import logging
from discord import app_commands 

# Classe para a criação de novos comandos
class SlashCommandBuilder(app_commands.Command):
    """
    Classe base para criação simplificada de comandos do tipo Slash (barra) com `discord.app_commands`.

    Essa classe exige que você implemente um método chamado `callback`, que será usado como o corpo do comando.

    Exemplo:
        class MeuComando(SlashCommandBuilder):
            def __init__(self, tree):
                super().__init__(app=tree, name="oi", description="Diz oi")

            async def callback(self, interaction: discord.Interaction):
                await interaction.response.send_message("Olá!")

    Args:
        app (app_commands.CommandTree): A árvore de comandos onde este comando será registrado.
        name (str): Nome do comando (usado no Discord).
        description (str): Descrição do comando que aparece para o usuário.

    Raises:
        NotImplementedError: Se a classe filha não implementar um método `callback`.
    """
    
    def __init__(
        self, 
        app: app_commands.CommandTree, 
        *, 
        name: str=None, 
        description:str=None
    ):
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