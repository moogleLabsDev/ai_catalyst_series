import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def generate_response(prompt):
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
        temperature=0,)
 
    response = completion.choices[0].message.content
    return response

prompt = input('\n**Prompt** ')
output = generate_response(f'read this prompt: {prompt}. Generate the text in plain format instead of bold. Keep your response short, crisp and in bullet format')
print(f'\n**Response** {output}')
