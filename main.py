import keyboard
from src.audio_recorder import record_audio
from src.audio_transcriber import transcribe_audio, delete_audio_file
from src.context_manager import ContextManager
from src.firekeeper_commands import process_command

AUDIO_FILE_PATH = "tmp/input_audio.wav"
context_manager = ContextManager(max_context_length=5)

print("Press `'` to record and interact with the Firekeeper.")

while True:
    if keyboard.is_pressed("'"):
        print("Recording audio...")
        record_audio(AUDIO_FILE_PATH)

        print("Transcribing audio...")
        try:
            transcription = transcribe_audio(AUDIO_FILE_PATH)
            print(f"Transcription: {transcription}")

            print("Generating Firekeeper response...")
            response = process_command(transcription, context_manager)  
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            delete_audio_file(AUDIO_FILE_PATH)
    
    # Add a small delay to prevent excessive CPU usage
    keyboard.wait('\'')  # Wait until the `'` key is released