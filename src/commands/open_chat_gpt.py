import os
import logging
import sys
import subprocess

def open_chrome_to_chatgpt():
    logging.info("Opening Chrome and navigating to ChatGPT")
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

        return "Opening Chrome... Proceed to ChatGPT, Ashen One. May your journey through the words bring clarity."

    except Exception as e:
        logging.error(f"Error opening Chrome: {str(e)}")
        return "Alas, an error has occurred in the execution of your request, Ashen One. Please try again."
