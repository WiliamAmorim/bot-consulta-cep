# Imagem base oficial do Python
FROM python:3.11-slim

# Evita gerar arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Evita buffering de logs
ENV PYTHONUNBUFFERED=1

# Diretório dentro do container
WORKDIR /app

# Copia apenas o requirements primeiro (melhora cache)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Comando para iniciar o bot
CMD ["python", "app/main.py"]