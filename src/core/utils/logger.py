"Sistema de logger gerado por Inteligência Artificial!"

import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Cria o diretório de logs se não existir
LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Configuração do formato do log
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def setup_logger(name: str) -> logging.Logger:
    """
    Configura e retorna um logger com handlers para console e arquivo.
    
    Args:
        name (str): Nome do logger (geralmente __name__ do módulo)
        
    Returns:
        logging.Logger: Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Evita duplicação de handlers
    if logger.handlers:
        return logger
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    console_handler.setFormatter(console_formatter)
    
    # Handler para arquivo (com rotação)
    log_file = os.path.join(LOGS_DIR, f"bot_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5*1024*1024,  # 5MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    file_handler.setFormatter(file_formatter)
    
    # Adiciona os handlers ao logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Logger padrão para o bot
bot_logger = setup_logger("discord_bot") 