# pip install openai

import openai

# Configurando o API Client
openai.api_key = 'your-api-key'

## Terminal: export OPENAI_API_KEY='your-api-key'

#  Escolhendo um modelo pré-treinado; listando-os
models = openai.Model.list()
print(models['data'])

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






