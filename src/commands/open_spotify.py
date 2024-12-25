import os
import logging
import sys
import subprocess
from src.gpt_4o_mini import get_firekeeper_response

def play_music(context_manager, command):
    logging.info("Playing music")
    
    try:
        spotify_path = r"C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe"
        system_message = {
            "role": "system",
            "content": "You are the Firekeeper, a guide for Ashen One. Acknowledge their request to play music through Spotify and provide a gentle response or maybe ask him what music he's going to play. Keep your response concise and limit it to no more than 3 sentences."
        }
        if sys.platform == "win32":
            if os.path.exists(spotify_path):
                logging.info(f"Running command: start {spotify_path}")
                subprocess.run(f"start {spotify_path}", shell=True, check=True)
            else:
                logging.error(f"Spotify not found at {spotify_path}")
                return "Spotify is not installed in the default location, Ashen One."
        elif sys.platform == "darwin":
            subprocess.run(["open", "-a", "Spotify"])
        elif sys.platform == "linux":
            subprocess.run(["spotify"])
        else:
            logging.error("Unsupported OS for opening Spotify")
            return "I am sorry, Ashen One... It seems your system cannot play the music at this time."

        return get_firekeeper_response(context_manager, command, system_message)

    except Exception as e:
        logging.error(f"Error opening Spotify: {str(e)}")
        return "An error occurred while opening Spotify, Ashen One... I will try again later."
