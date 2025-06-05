# Template for bot's with Python and discord.py

(em desenvolvimento...)

#### Esse projeto é uma base/ambiente que visa acelerar e abstrair o desenvolvimento de bots para discord utilizando a linguagem de programação Python e a biblioteca discord.py, de forma estruturada e organizada.


### Os builders disponíveis são:


| Builder                | Função                                                                                                                   |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `CommandBuilder`       | **Responsável pela criação de comandos para o bot.**                                                                    |
| `ButtonBuilder`        | **Responsável pela criação de botões no Discord (Herda de discord.ui.Button).**                                        |
| `ComponentBuilder`     | **Responsável por adicionar componentes (botões, modals, selects) à uma view (Herda de discord.ui.View).**              |
| `InputTextBuilder`     | **Responsável pela criação de InputTexts/Fields para a modal (ModalBuilder) (Herda de discord.ui.TextInput).**          |
| `ModalBuilder`         | **Responsável pela criação de modais no Discord (Herda de discord.ui.Modal).**                                          |
| `SelectOptionBuilder`  | **Responsável pela criação de opções para um futuro SelectMenu (SelectMenuBuilder) (Herda de discord.SelectOption).** |
| `SelectMenuBuilder`    | **Responsável pela criação de um SelectMenu no Discord (Herda de discord.ui.Select).**                                  |
| `SelectUserBuilder`    | **Responsável pela criação de um SelectMenu de membros do servidor (Herda de discord.ui.UserSelect).**                  |
| `SelectRoleBuilder`    | **Responsável pela criação de um SelectMenu de roles/cargos do servidor (Herda de discord.ui.RoleSelect).**             |
| `SelectChannelBuilder` | **Responsável pela criação de um SelectMenu de canais do servidor (Herda de discord.ui.ChannelSelect).**                |

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
