import os
import requests
import json
from dotenv import load_dotenv

load_dotenv('.env')

C_PROMPT = """
You need to summarize the attached file in JSON format. You will read financial reports and must extract relevant financial data.

# Output format 
Always output the following JSON format:
{
	"company": "name",
	"coupon_date": "date",
	"maturity_date": "date",
	"issue_date": "date",
	"coupon_frequency": "frequency"
}

# Input File:
"""

def send_to_gpt(prompt):
    url = "https://api.openai.com/v1/chat/completions"  # Changed endpoint to chat completions
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }
    data = {
        "model": "gpt-4-turbo",  # Ensure the model is specified if needed
        "messages": [{"role": "user", "content": prompt}],  # Structured for chat completion
        "max_tokens": 150,
        "temperature": 0.5,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get response from GPT: {response.text}")


def save_json(data, filename):
    with open(filename, 'w') as f:
        #json.dump(data, f, indent=4)
        f.write(data)

def read_and_process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                response = send_to_gpt(C_PROMPT+"\n"+content)
                output_filename = os.path.splitext(filename)[0] + '.json'
                save_json(response["choices"][0]["message"]["content"], os.path.join(directory, output_filename))
                print(f"Saved GPT response for {filename} as {output_filename}")

read_and_process_files('output')
