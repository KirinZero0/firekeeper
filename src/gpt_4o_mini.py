import openai
import json
import os

def load_api_key():
    """Loads API keys from a JSON file."""
    api_key_path = os.path.join(os.path.dirname(__file__), '../config/api_keys.json')
    
    if not os.path.exists(api_key_path):
        raise FileNotFoundError(f"API key file not found: {api_key_path}")
    
    with open(api_key_path, "r") as file:
        keys = json.load(file)
    return keys["openai_api_key"]

def get_firekeeper_response(context_manager, prompt, max_tokens=100):
    """Generates a response in the style of Firekeeper using GPT-4."""
    context = context_manager.format_context_for_api()
    
    system_message = {
        "role": "system",
        "content": "You are the Firekeeper, a mystical guide for Ashen One. Answer like the Firekeeper from Dark Souls 3. Keep your responses concise, no more than 3 sentences, unless the user asks for complete information."
    }
    context.append({"role": "user", "content": prompt})

    context.insert(0, system_message)
    print(context)
    openai.api_key = load_api_key()
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=context,
        max_tokens=max_tokens 
    )
    firekeeper_response = response.choices[0].message.content

    context_manager.add_exchange(prompt, firekeeper_response)

    return firekeeper_response