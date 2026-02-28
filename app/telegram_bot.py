import re
import logging
from telegram import Update
from telegram.ext import ContextTypes
from services.viacep_service import consultar_cep
from services.geolocation_service import obter_coordenadas

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 Bot Consulta CEP\n\nUse:\n/cep 01001000"
    )

async def cep(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "❌ Você precisa informar um CEP.\nExemplo: /cep 01001000"
        )
        return

    cep_digitado = context.args[0].replace("-", "").strip()

    if not re.fullmatch(r"\d{8}", cep_digitado):
        await update.message.reply_text(
            "❌ O CEP deve conter exatamente 8 números."
        )
        return

    dados = consultar_cep(cep_digitado)

    if not dados:
        await update.message.reply_text("❌ CEP não encontrado.")
        return

    resposta = (
        f"📍 Endereço encontrado:\n\n"
        f"Rua: {dados.get('logradouro', 'Não informado')}\n"
        f"Bairro: {dados.get('bairro', 'Não informado')}\n"
        f"Cidade: {dados['localidade']} - {dados['uf']}\n"
        f"CEP: {dados['cep']}"
    )

    await update.message.reply_text(resposta)

    endereco_completo = f"{dados['logradouro']}, {dados['localidade']}, {dados['uf']}, Brasil"
    coords = obter_coordenadas(endereco_completo)

    if coords:
        latitude, longitude = coords
        await update.message.reply_location(latitude=latitude, longitude=longitude)

async def mensagem_invalida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Comando inválido. Use /cep 01001000")