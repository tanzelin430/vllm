from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="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",
)

completion = client.chat.completions.create(
  model="meta-llama/Llama-2-13b-hf",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)