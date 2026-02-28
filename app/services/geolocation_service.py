import requests
import logging

logger = logging.getLogger(__name__)

def obter_coordenadas(endereco_completo: str):
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": endereco_completo,
            "format": "json",
            "limit": 1
        }

        headers = {
            "User-Agent": "BotCEP/1.0"
        }

        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        dados = response.json()

        if not dados:
            logger.warning(f"Coordenadas não encontradas: {endereco_completo}")
            return None

        logger.info(f"Coordenadas obtidas: {endereco_completo}")
        return float(dados[0]["lat"]), float(dados[0]["lon"])

    except requests.RequestException as e:
        logger.error(f"Erro ao obter coordenadas: {e}")
        return None