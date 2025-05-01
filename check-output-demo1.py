from openai import OpenAI
from tool import getClient

client = getClient()

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}]
)

print(response.choices[0].message.content)