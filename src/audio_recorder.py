import sounddevice as sd
import wave
import keyboard

def record_audio(file_path, samplerate=44100):
    """Records audio while holding a key and saves it to a file."""
    print("Press and hold the `'` key to start recording...")
    
    # Wait until the user presses the key to start recording
    while not keyboard.is_pressed("'"):
        pass

    # Start recording once the key is pressed
    print("Recording... Speak now!")
    audio_data = []
    with sd.InputStream(samplerate=samplerate, channels=1, dtype='int16') as stream:
        while keyboard.is_pressed("'"):  # Continue recording as long as the key is held
            chunk, overflowed = stream.read(samplerate)
            audio_data.append(chunk)
    
    # Flatten the list of chunks
    audio_data = b''.join([chunk.tobytes() for chunk in audio_data])
    
    # Save the audio to a file
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data)

    print(f"Audio recorded and saved to {file_path}.")