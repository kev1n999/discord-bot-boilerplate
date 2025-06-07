from core.utils.logger import bot_logger

if __name__ == "__main__":
    try:
        from core.client.client import client
        bot_logger.info("Iniciando o bot...")
        # inicia o bot a partir do token passado
        client.run_bot()
    except Exception as e:
        bot_logger.error(f"Erro ao iniciar o bot: {str(e)}", exc_info=True)