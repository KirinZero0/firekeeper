import os
import logging
import sys
import subprocess

def play_music():
    logging.info("Playing music")
    
    try:
        spotify_path = r"C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe"

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

        return "Ah, Ashen One... I have opened Spotify for you. Enjoy the melodies of the world."

    except Exception as e:
        logging.error(f"Error opening Spotify: {str(e)}")
        return "An error occurred while opening Spotify, Ashen One... I will try again later."
