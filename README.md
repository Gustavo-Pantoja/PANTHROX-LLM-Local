🤖 PANTHROX – Chat com LLM Local (LM Studio + Python)

Este projeto demonstra como se comunicar com um modelo de linguagem local (LLM) utilizando Python e a API compatível com OpenAI fornecida pelo LM Studio.

A aplicação envia perguntas para um modelo local e recebe respostas diretamente no terminal, simulando um chat simples com Inteligência Artificial.

🚀 Tecnologias utilizadas

- Python 3
- LM Studio
- API compatível com OpenAI
- VS Code
- Ambiente virtual (.venv)

🧠 Arquitetura do projeto

Fluxo da aplicação:
Usuário → Script Python → API Endpoint → LM Studio → Modelo LLM → Resposta no Terminal

O script Python envia requisições para o servidor local do LM Studio utilizando um endpoint compatível com a API da OpenAI.

📦 Instalação

- Clone o repositório:
- git clone https://github.com/Gustavo-Pantoja/PANTHROX-LLM-Local.git
- Entre na pasta do projeto:
- cd PANTHROX-LLM-Local
- Crie o ambiente virtual:
- python -m venv .venv
- Ative o ambiente virtual:
- Windows (PowerShell)
- .venv\Scripts\Activate
- Instale as dependências:

pip install -r requirements.txt

▶️ Executando o projeto

- Certifique-se de que o LM Studio esteja rodando com o Local Server ativo.
- Depois execute:
- python chat_client.py
- Digite sua pergunta no terminal:

Você: O que é inteligência artificial?

A resposta da IA será exibida diretamente no terminal.

🔑 Configuração da API

- O endpoint local é configurado no código:
- base_url="http://127.0.0.1:1234/v1"
- A API Key pode ser qualquer valor caso a autenticação esteja desativada no LM Studio.
- Para maior segurança recomenda-se utilizar variáveis de ambiente (.env).

📊 Exemplo de uso

Você: Explique o que é Machine Learning.

IA: Machine Learning é uma área da inteligência artificial que permite que sistemas aprendam a partir de dados sem serem explicitamente programados.

🎯 Objetivo do projeto

- Este projeto foi desenvolvido para estudar:
- Integração com APIs de modelos de linguagem
- Uso de LLMs localmente
- Comunicação entre Python e servidores de IA
- Estruturação de projetos Python

📚 Possíveis melhorias

- Implementar memória persistente de conversa
- Criar interface web
- Implementar streaming de respostas
- Adicionar suporte a múltiplos modelos
- Containerização com Docker

👨‍💻 Autor

Gustavo Pantoja
Projeto desenvolvido como parte dos estudos em Inteligência Artificial, APIs e desenvolvimento Python.
