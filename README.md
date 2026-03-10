🤖 Chat com IA Local usando LM Studio + Python

Este projeto demonstra como se comunicar com um modelo de linguagem local (LLM) através de uma API utilizando Python.

A aplicação utiliza o servidor local do LM Studio para enviar perguntas e receber respostas diretamente no terminal, simulando um chat simples com Inteligência Artificial.

🚀 Tecnologias utilizadas

Python 3
LM Studio
API compatível com OpenAI
VSCode
Ambiente virtual (.venv)

   ====

🧠 Como funciona

O script Python envia requisições HTTP para o servidor local do LM Studio usando:
API Key
Endpoint local
Fluxo da aplicação:
Usuário → Python Script → API Endpoint → LM Studio → Modelo LLM → Resposta no terminal

   ====

📦 Instalação
Clone o repositório:
git clone https://github.com/seuusuario/nome-do-repo.git
Entre na pasta:
cd nome-do-repo
Crie o ambiente virtual:
python -m venv .venv
Ative o ambiente:
Windows (PowerShell)
.venv\Scripts\Activate
Instale as dependências:
pip install openai

   ====

▶️ Executando o projeto

Certifique-se de que o LM Studio esteja rodando com o Local Server ativo.
Depois execute:
python chat_local.py
Digite sua pergunta no terminal:
Você: O que é inteligência artificial?
Resposta da IA será exibida diretamente no terminal.

   ====

🔑 Configuração da API

No código, o endpoint local é configurado assim:
base_url="http://127.0.0.1:1234/v1"
A API Key pode ser qualquer valor caso a autenticação esteja desativada no LM Studio.

   ====

📊 Exemplo de funcionamento

Você: Explique o que é Machine Learning.

IA: Machine Learning é uma área da inteligência artificial que permite que sistemas aprendam a partir de dados sem serem explicitamente programados.

   ====

🎯 Objetivo do projeto

Este projeto foi desenvolvido para aprender:
Integração com APIs de modelos de linguagem
Uso de LLMs localmente
Comunicação entre Python e servidores de IA

   ====

📚 Possíveis melhorias

Implementar memória de conversa
Criar interface web
Implementar streaming de respostas
Adicionar suporte a múltiplos modelos

   ====

👨‍💻 Autor

Projeto desenvolvido por Gustavo Pantoja como parte dos estudos em Inteligência Artificial e desenvolvimento Python.
