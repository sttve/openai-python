# pip install openai

import openai

## Terminal: export OPENAI_API_KEY='your-api-key'


# Configurando o API Client
openai.api_key = 'your-api-key'


# Definindo o prompt
prompt = "What I need study to develop my career in Python?"

# Gerando texto baseado em prompt
response = openai.Completion.create(
    engine="davinci"
    prompt=prompt,
    max_tokens=50
)

# Imprimindo o texto gerado
print(response.choices[0].text)






