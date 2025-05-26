import discord 
import logging
from typing import Union, List, Coroutine

class InputTextBuilder(discord.ui.TextInput):
    """
    Builder personalizado para criar campos de entrada (`TextInput`) em modais do Discord.

    Permite configurar o estilo, placeholder, se é obrigatório, entre outros.

    Args:
        label (str): Texto do título do campo. Obrigatório.
        placeholder (str, optional): Texto de dica exibido dentro do campo. Padrão é None.
        style (str | discord.TextStyle, optional): Estilo do campo: 'short', 'long' ou 'paragraph'. Padrão é 'short'.
        custom_id (str, optional): ID único do campo, usado para recuperar o valor após envio. Padrão é None.
        required (bool, optional): Define se o campo é obrigatório. Padrão é True.

    Raises:
        TypeError: Se `label` não for informado.
        logging.error: Se o estilo informado não for reconhecido.
    """
    
    def __init__(
        self, 
        label: str, 
        placeholder: str=None, 
        style:str | discord.TextStyle=None, 
        custom_id: str | None=None, 
        required: bool=None
    ):
        self.text_styles = {
            "short": discord.TextStyle.short ,
            "long": discord.TextStyle.long,
            "paragraph": discord.TextStyle.paragraph
        } 
        
        if not label:
            raise TypeError("Erro: Label não informado na criação do InputText!")

        if style is None:
            style = self.text_styles["short"]
        else:    
            if not style in self.text_styles.keys():
                logging.error(f"[⚠] O estilo {style} não existe! Os estilos disponíveis para InputTexts são: [short, long, paragraph]")
            else:
                style = self.text_styles[style.lower()]
            
        super().__init__(
            label=label,
            style=style,
            placeholder=placeholder,
            custom_id=custom_id, 
            required=required if required else True
        )
        
class ModalBuilder(discord.ui.Modal):
    """
    Builder personalizado para criar modais (`discord.ui.Modal`) com suporte para listener e validação automática.

    Permite adicionar até 5 `InputTextBuilder`s. Quando o modal for enviado, `modal_listener` será chamado.

    Args:
        title (str, optional): Título do modal exibido no Discord.
        custom_id (str, optional): ID único do modal.
        persistent (bool, optional): Se True, o modal não terá timeout. Padrão é False (180s).
        items (Union[List[InputTextBuilder], InputTextBuilder]):
            Um campo ou uma lista de campos de texto a serem exibidos no modal.
        modal_listener (Coroutine): Função assíncrona a ser chamada quando o modal for enviado.

    Raises:
        TypeError: Se nenhum item for passado.
        logging.error: Se forem passados mais de 5 itens.
        logging.error: Se `modal_listener` não for definido no envio do modal.

    Exemplo:
        async def meu_listener(interaction):
            valor = interaction.data['components'][0]['components'][0]['value']
            await interaction.response.send_message(f"Você escreveu: {valor}")

        campo = InputTextBuilder(label="Nome", placeholder="Digite seu nome")
        modal = ModalBuilder(title="Formulário", items=campo, modal_listener=meu_listener)
        await interaction.response.send_modal(modal)
    """
    
    def __init__(
        self, 
        title: str=None, 
        custom_id: str=None, 
        persistent: bool=None, 
        *, 
        items: Union[List[InputTextBuilder], InputTextBuilder]=None, 
        modal_listener: Coroutine
    ):
        self.modal_listener = modal_listener
        
        if items is None:
            raise TypeError("Erro: Nenhum item foi passado!")
            
        super().__init__(
            title=title,
            timeout=None if persistent else 180,
            custom_id=custom_id
        )
        
        if isinstance(items, list):
            if len(items) > 5:
                logging.error("[⚠] As modais podem ter no máximo 5 itens!")
                items = items[:5]
                
            for item in items:
                self.add_item(item)
        else:
            self.add_item(items)
    
    async def on_submit(self, interaction: discord.Interaction):
        if not self.modal_listener:
            logging.error("[⚠] Você não passou nenhuma função para o paramêtro 'modal_listener'!")
            return 
        
        await self.modal_listener(interaction)