from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.2.162:1234/v1",
    api_key="sk-lm-LcwWrkf5:8lkAe3gCJ5ezzNVRxVee",
)

while True:

    pergunta = input("Você: ")

    resposta = client.chat.completions.create(
        model="mistral-7b-instruct", messages=[{"role": "user", "content": pergunta}]
    )

    print("IA:", resposta.choices[0].message.content)
