import requests
import logging

logger = logging.getLogger(__name__)

def consultar_cep(cep: str) -> dict | None:
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        dados = response.json()

        if "erro" in dados:
            logger.warning(f"CEP não encontrado: {cep}")
            return None

        logger.info(f"CEP consultado com sucesso: {cep}")
        return dados

    except requests.RequestException as e:
        logger.error(f"Erro ao consultar ViaCEP: {e}")
        return None