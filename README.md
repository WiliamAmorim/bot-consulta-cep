📍 Bot de Consulta de CEP com Telegram

Bot desenvolvido em Python que realiza consulta de CEP utilizando a API pública do ViaCEP e retorna:

✅ Endereço completo

✅ Cidade e Estado

✅ Localização no mapa (latitude e longitude)

✅ Log estruturado das consultas

O projeto foi estruturado seguindo boas práticas de arquitetura modular, separação de responsabilidades e uso de variáveis de ambiente para segurança.

🚀 Tecnologias Utilizadas

🐍 Python 3.10+

🤖 python-telegram-bot

🌐 Requests

🔐 python-dotenv

📦 API pública ViaCEP

🗺 API pública OpenStreetMap (Nominatim)

🐳 Docker

🏗 Arquitetura do Projeto

bot_consulta_cep/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── telegram_bot.py
│   ├── config.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── viacep_service.py
│   │   └── geolocation_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger_config.py
│   └── logs/
│       └── bot.log
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

🔹 Separação de Responsabilidades

main.py → Inicialização do bot

telegram_bot.py → Handlers e regras de interação

viacep_service.py → Consulta à API ViaCEP

geolocation_service.py → Obtenção de coordenadas

logger_config.py → Configuração de logs

🔐 Segurança

O token do Telegram é armazenado em variável de ambiente utilizando .env.

Exemplo:

TELEGRAM_TOKEN=SEU_TOKEN_AQUI

O arquivo .env está protegido no .gitignore.

📊 Funcionalidades

✔ Validação rigorosa de CEP (8 dígitos)

✔ Tratamento de exceções com try/except

✔ Timeout nas requisições HTTP

✔ Registro de logs das consultas

✔ Retorno de localização geográfica no Telegram

✔ Estrutura pronta para escalar

🖥 Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/WiliamAmorim/bot_consulta_cep.git
cd bot_consulta_cep
2️⃣ Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Criar arquivo .env
TELEGRAM_TOKEN=SEU_TOKEN_AQUI
5️⃣ Executar
python app/main.py
📁 Logs

Todas as consultas são registradas em:

logs/bot.log

Isso permite auditoria e rastreabilidade das requisições.

---

## 🐳 Executando com Docker
###
1️⃣ Baixar a imagem

bash:
docker pull wiliamamorim/bot-cep:1.0

2️⃣ Executar o container
docker run -e TELEGRAM_TOKEN=SEU_TOKEN \
  -v ./logs:/app/logs \
  wiliamamorim/bot-cep:1.0
  📦 Docker Hub

Imagem disponível em:
https://hub.docker.com/r/wiliamamorim/bot-cep


💡 Possíveis Melhorias Futuras

Deploy em VPS ou serviço cloud

Implementação de testes automatizados

Limitação de requisições (rate limit)

Banco de dados para histórico de consultas

Interface Web complementar

👨‍💻 Sobre o Projeto

Este projeto foi desenvolvido como parte da construção de portfólio focado em:

Automação com Python

Integração com APIs públicas

Desenvolvimento de bots para negócios

Estruturação profissional de projetos

📌 Aplicações Práticas

Este bot pode ser utilizado para:

🏢 Imobiliárias

📦 Logística e entregas

🏪 Pequenos negócios

🧾 Validação de cadastro

📊 Automação administrativa

⭐ Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests.