# Simple Chat Bot Example

## Usage
Python 3.10.10  
Create a virtual environment and restore dependencies  
`export OPENAI_API_KEY=<YourAPIKey>`
`python app.py`  

`load_document()` loads files from disk and indexes them (does not need API key).  
`generate_response()` calls the openai Completion API endpoint (requires API key)

## Todo

* This appears to use GPT2 for indexing. Need to verify.

## Source
* https://hackthedeveloper.com/openai-chatgpt-api-python-guide/  
* https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5
