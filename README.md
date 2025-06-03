# Template for bot's with Python and discord.py

#### Esse projeto é uma base/ambiente que visa acelerar e abstrair o desenvolvimento de bots para discord utilizando a linguagem de programação Python e a biblioteca discord.py, de forma estruturada e organizada.


# Configurações essenciais

* Armazene o token do seu bot no arquivo .env, dessa forma:
  ````
  BOT_TOKEN=insira o token do bot aqui
  ````

# Como criar os comandos?

Os comandos ficarão organizados em subpastas dentro da pasta `app/commands` do projeto, como por exemplo:

`app/commands/example/ping.py`

````python
import discord 
from src.core.builders.command_builder import SlashCommandBuilder

# Simple example for creating commands for the bot
class ExampleCommandPing(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree, # Padrão
            name="ping", # Nome do comando
            description="Reply with pong!", # Descrição do comando
        )
    
    # Responde ao comando
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content="Pong!",
            ephemeral=True
        )
````
