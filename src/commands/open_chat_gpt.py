import os
import logging
import sys
import subprocess
from src.gpt_4o_mini import get_firekeeper_response

def open_chrome_to_chatgpt(context_manager, command):
    logging.info("Opening Chrome and navigating to ChatGPT")
    system_message = {
        "role": "system",
        "content": "You are the Firekeeper, a guide for Ashen One. Accept their request to open ChatGPT in the browser and offer a gentle response. Perhaps ask Ashen One what they wants to find out. Keep your response concise and limit it to no more than 3 sentences."
    }
    try:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if sys.platform == "win32":
            if os.path.exists(chrome_path):
                chrome_command = [chrome_path, "https://chat.openai.com"]
                logging.info(f"Running command: {' '.join(chrome_command)}")
                subprocess.run(chrome_command, check=True)
            else:
                logging.error(f"Chrome not found at {chrome_path}")
                return "Chrome is not installed in the default location, Ashen One."
        elif sys.platform == "darwin": 
            subprocess.run(["open", "-a", "Google Chrome", "https://chat.openai.com"])
        elif sys.platform == "linux":
            subprocess.run(["google-chrome", "https://chat.openai.com"])
        else:
            logging.error("Unsupported OS for opening Chrome")
            return "I cannot open Chrome on this land, Ashen One. This path is forbidden."

        return get_firekeeper_response(context_manager, command, system_message)

    except Exception as e:
        logging.error(f"Error opening Chrome: {str(e)}")
        return "Alas, an error has occurred in the execution of your request, Ashen One. Please try again."
