import os

def get_token():
    token = os.getenv("TELEGRAM_TOKEN")

    if not token:
        raise ValueError(
            "Nenhuma variável TELEGRAM_TOKEN ou TOKEN configurada"
        )
    return token
