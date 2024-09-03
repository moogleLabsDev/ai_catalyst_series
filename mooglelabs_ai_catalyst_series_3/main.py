import os
import base64
import requests
from dotenv import load_dotenv
from openai import OpenAI
from template import zero_shot_prompt, one_shot_prompt, few_shot_prompt, chain_of_thought_prompt, rag_prompt, tree_of_thoughts_prompt, multimodal_prompt, meta_prompting, adversarial_prompt, query_transformation_prompt, brainstorm_ideas_prompt, copy_generation_prompt, client_support_prompt, generate_analogies_prompt, bulk_copy_generation_prompt


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def generate_response(pmt):
    if isinstance(pmt, dict):
        image_path = pmt["path"]
        txt = pmt["prompt"]
        base64_image = encode_image(image_path)

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
        }

        payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": txt
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300}

        print(f'\n**Prompt** {txt}')
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']

    else:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful creative assistant."},
                {"role": "user", "content": pmt},
            ],
            temperature=0.5,)

    print(f'\n**Prompt** {prompt}')
    response = completion.choices[0].message.content
    return response

prompt = bulk_copy_generation_prompt
print("**Response**", generate_response(prompt))
