# API de Pagamentos PIX com Flask

Este é um projeto de API para processamento de pagamentos PIX utilizando Flask, SQLAlchemy e WebSocket para comunicação em tempo real.

## 🚀 Funcionalidades

- Criação de pagamentos PIX
- Geração de QR Code para pagamento
- Confirmação de pagamentos via webhook
- Interface web para visualização do status do pagamento
- Notificações em tempo real via WebSocket
- Sistema de expiração de pagamentos (30 minutos)

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-SocketIO
- SQLite
- qrcode
- HTML/CSS/JavaScript

## 📋 Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. Inicie o servidor:
```bash
python app.py
```

2. Acesse a aplicação:
- Interface web: http://localhost:5000
- API: http://localhost:5000/payments/pix

## 📝 Endpoints da API

### Criar Pagamento PIX
- **POST** `/payments/pix`
- Body:
```json
{
    "value": 100.00
}
```

### Confirmar Pagamento
- **POST** `/payments/pix/confirmation`
- Body:
```json
{
    "bank_payment_id": "id_do_pagamento",
    "value": 100.00
}
```

### Visualizar Pagamento
- **GET** `/payments/pix/<payment_id>`

## 📁 Estrutura do Projeto

```
├── app.py                 # Arquivo principal da aplicação
├── requirements.txt       # Dependências do projeto
├── static/               # Arquivos estáticos
│   ├── css/             # Estilos CSS
│   ├── img/             # Imagens geradas (QR Codes)
│   └── template_img/    # Imagens do template
├── templates/           # Templates HTML
│   ├── payment.html
│   ├── confirmed_payment.html
│   └── 404.html
├── repository/          # Configurações do banco de dados
├── db_models/          # Modelos do banco de dados
└── payments/           # Lógica de pagamentos
```

## 🧪 Testes

Para executar os testes:
```bash
pytest tests/
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 