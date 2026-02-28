import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram_bot import start, cep, mensagem_invalida
from utils.logger_config import setup_logger
from config import get_token

def main():
    token = get_token()
    print("Token carregado com sucesso.")

    load_dotenv()
    logger = setup_logger()

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cep", cep))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem_invalida))

    logger.info("Bot iniciado com sucesso.")
    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()