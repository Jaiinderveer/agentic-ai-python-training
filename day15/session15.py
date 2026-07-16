from openai import OpenAI

openai_api_key = open('day15/api_key.txt','r').read().strip()

client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a one-sentence about agentic ai."
)

print(response.output_text)