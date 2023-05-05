## 🤖 OpenAI em Python

### Procedimentos

1. Primeiro, você precisa se inscrever para uma chave de API OpenAI. Você pode fazer isso visitando o site da OpenAI e seguindo as instruções para criar uma conta.

2. Depois de ter sua chave de API, você pode instalar o pacote OpenAI Python usando pip.<br/>Abra seu terminal ou prompt de comando e digite o seguinte comando:

```bash
pip install openai
```
3. Depois de instalar o pacote, você pode importá-lo em seu código Python usando a seguinte linha:

```bash
import openai

openai.api_key = "YOUR_API_KEY"
```
4. OpenAI fornece uma variedade de modelos pré-treinados que você pode usar para várias tarefas, como processamento de linguagem natural ou reconhecimento de imagem.<br/>Para escolher um modelo pré-treinado, você pode usar a função abaixo para ver uma lista de modelos disponíveis:

```bash
models = openai.Model.list()
print(models['data'])
```
5. Depois de escolher um modelo, você pode usá-lo para gerar a saída passando um prompt para a função:
```bash
openai.Completion.create
```
### 🦾 Substitua 'your-api-key' pela sua chave de API real.
Agora você pode começar a usar a API OpenAI em seu código Python!<br/>
Esse código gerará 50 tokens de texto com base no prompt inserido usando o mecanismo da sua escolha e imprimindo o texto gerado no console.
