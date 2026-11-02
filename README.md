# ATLAS — Assistente pessoal

> Projeto em desenvolvimento

O **ATLAS** é um projeto de assistente pessoal que busca reunir interação por texto e voz em uma interface própria, conectada a um backend responsável por interpretar comandos e direcioná-los para funcionalidades específicas.

A ideia é construir uma base modular: comandos conhecidos são tratados por componentes próprios, enquanto solicitações mais abertas poderão ser encaminhadas a uma camada de inteligência artificial no futuro.

## ✨ Visão do projeto

- Interface web para interação com o assistente
- Entrada de comandos por texto e voz
- Backend em Python com FastAPI
- Interpretação e classificação de comandos
- Dispatcher para encaminhar comandos aos serviços responsáveis
- Estrutura preparada para expansão gradual de funcionalidades

## 🧱 Tecnologias

- **Backend:** Python, FastAPI, Pydantic
- **Persistência:** SQLAlchemy e PostgreSQL (em desenvolvimento)
- **Frontend:** HTML, CSS e JavaScript
- **Servidor:** Uvicorn

## 🗂️ Organização atual

```text
ATLAS0.1/
├── backend/
│   └── app/
│       ├── config/
│       ├── database/
│       ├── dispatcher/
│       ├── interpreter/
│       ├── models/
│       ├── providers/
│       ├── repositories/
│       ├── routes/
│       ├── schemas/
│       ├── security/
│       ├── services/
│       └── main.py
├── frontend/
│   ├── css/
│   ├── img/
│   ├── js/
│   ├── index.html
│   └── login.html
└── requirements.txt
```

## ⚙️ Executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Isaias-Morais/ATLAS0.1.git
cd ATLAS0.1
```

### 2. Criar e ativar o ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Configure as variáveis necessárias para o ambiente local em um arquivo `.env`. Não envie credenciais, tokens ou chaves privadas para o GitHub.

### 5. Iniciar a API

Na raiz do projeto:

```bash
uvicorn backend.app.main:app --reload
```

A documentação interativa do FastAPI, quando a API estiver em execução, fica disponível em:

- http://127.0.0.1:8000/docs

> A execução completa depende das configurações e dos serviços definidos no ambiente local.

## 🛠️ Status

O ATLAS está em desenvolvimento. A estrutura inicial do backend e da interface está sendo construída e evoluída por etapas. Funcionalidades, integrações e fluxos ainda podem mudar.

## 🧭 Próximas etapas

- Consolidar o fluxo de interpretação e despacho de comandos
- Evoluir os serviços de lembretes e música
- Integrar de forma consistente a interface com a API
- Ampliar validações e testes automatizados
- Documentar as funcionalidades conforme forem concluídas

## 👨‍💻 Autor

Desenvolvido por **[Isaias Morais](https://github.com/Isaias-Morais)** como projeto prático de estudo e evolução em desenvolvimento de software.
