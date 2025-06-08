# Template for bot's with Python and discord.py

(em desenvolvimento...)

#### Esse projeto é uma base/ambiente que visa acelerar e abstrair o desenvolvimento de bots para discord utilizando a linguagem de programação Python, baseado principalmente na biblioteca [discord.py](https://discordpy.readthedocs.io/en/stable/), de forma estruturada e organizada.

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


# Como criar e enviar componentes com comandos?

Os componentes podem ser criados usando os builders e enviados junto com as respostas dos comandos. Exemplo básico:

```python

import discord
from core.builders.command_builder import SlashCommandBuilder
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder

class ExampleCommand(SlashCommandBuilder):
    def __init__(self, tree) -> None:
        super().__init__(
            app=tree,
            name="exemplo",
            description="Exemplo de comando com componentes"
        )
  
    async def callback(self, interaction: discord.Interaction) -> None:
        # Criando um botão
        button = ButtonBuilder(
            label="Clique aqui!",
            style=discord.ButtonStyle.primary,
            custom_id="exemplo_botao"
        )
  
        # Criando e enviando o botão
        component_button = ComponentBuilder(button) # Também aceita uma lista([]) de de builders, como: [button1, button2]

        await interaction.response.send_message(
          content="Mensagem com botão",
          view=component_button
        )
```

### Tipos de Componentes Disponíveis:

1. **Botões** (`ButtonBuilder`):

   - Botões interativos com diferentes estilos
   - Útil para ações simples
2. **Select Menus** (`SelectMenuBuilder`):

   - Menus dropdown com opções personalizadas
   - Suporta seleção de usuários, cargos e canais
3. **Modais** (`ModalBuilder`):

   - Formulários com campos de texto
   - Ideal para coletar informações do usuário

Todos os builders estão disponíveis em `src/core/builders/` e seguem o mesmo padrão de uso.
