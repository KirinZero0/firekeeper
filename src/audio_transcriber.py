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

def transcribe_audio(file_path):
    """Transcribes audio using OpenAI Whisper API."""
    openai.api_key = load_api_key()
    with open(file_path, "rb") as audio_file:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="en"
        )
    return response.text

def delete_audio_file(file_path):
    """Deletes the audio file after processing."""
    if os.path.exists(file_path):
        os.remove(file_path)
