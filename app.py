import os
from os.path import exists
from timeit import default_timer

import openai
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

openai.api_key = os.environ.get('OPENAI_API_KEY')

def load_document():
    start = default_timer()
    if not exists('index/index.json'):
        documents = SimpleDirectoryReader('data').load_data()
        index = GPTSimpleVectorIndex(documents)
        index.save_to_disk('index/index.json')
    index = GPTSimpleVectorIndex.load_from_disk('index/index.json')
    print(f'Document loaded and indexed in {default_timer() - start} seconds')
    return index


def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

index = load_document()
prompt = input('Ask me a question (Ctrl-c to quit): ')
while (1):
    # response = generate_response(prompt)
    response = index.query(prompt)
    print(response)
    prompt = input('Ask another question: ')
