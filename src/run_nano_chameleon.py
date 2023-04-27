import os
import openai
import requests
import json
import pathlib


from dotenv import load_dotenv
load_dotenv()

def call_chatgpt(prompt):
    reqUrl = 'https://api.openai.com/v1/chat/completions'
    headers = { 
                'Authorization': "Bearer " + os.getenv("OPENAI_API_KEY"),
                'Content-Type': "application/json"
              }
    data = { 
             'model': 'gpt-3.5-turbo',
             'messages': [
                            { 
                                "content": prompt,
                                "role": "user"
                            }
                         ]
            }
    response = requests.post(reqUrl, headers=headers, json=data)
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = json.loads(line.decode('utf-8'))
                generated_text = decoded_line['choices'][0]['message']["content"].strip()
                print("Generated text: ", generated_text)
    else:
        print("Error: ", response.status_code, response.text)

# if __name__ == '__main__':
#    call_chatgpt("Tell me the most relevant information about Chameleon.")

if __name__ == '__main__':
    #file_path = os.path.abspath()
    #print(os.listdir())
    with open('demos/prompt_metadata.py', 'r') as f:
        prompt = f.read().split('prompt = """')[1].split('"""')[0]
    call_chatgpt(prompt)
