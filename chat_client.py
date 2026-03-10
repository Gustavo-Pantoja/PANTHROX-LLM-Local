from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

client = OpenAI(base_url=API_URL, api_key=API_KEY)

model = "mistral-7b-instruct"
arquivo_memoria = "historico.json"


def carregar_historico():
    if os.path.exists(arquivo_memoria):
        with open(arquivo_memoria, "r", encoding="utf-8") as f:
            return json.load(f)
    return [{"role": "system", "content": "Você é um assistente útil e objetivo."}]


def salvar_historico(messages):
    with open(arquivo_memoria, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)


messages = carregar_historico()

print("Chat iniciado. Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    messages.append({"role": "user", "content": pergunta})

    try:
        resposta = client.chat.completions.create(
            model=model,
            messages=messages
        )

        texto = resposta.choices[0].message.content

        print("IA:", texto, "\n")

        messages.append({"role": "assistant", "content": texto})

        salvar_historico(messages)

    except Exception as e:
        print("Erro ao consultar a IA:", e)