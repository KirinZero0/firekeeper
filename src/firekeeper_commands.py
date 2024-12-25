import os
import logging
import sys
import subprocess
import re
from src.gpt_4o_mini import get_firekeeper_response
from src.commands.open_chat_gpt import open_chrome_to_chatgpt
from src.commands.shutdown_pc import shutdown_pc
from src.commands.open_spotify import play_music
from src.commands.system_status import check_system_status

log_directory = "logs"
os.makedirs(log_directory, exist_ok=True) 

logging.basicConfig(
    filename=os.path.join(log_directory, 'firekeeper_commands.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def handle_command(command, context_manager):
    command = command.lower()

    try:
        if re.search(r"(chat|gpt).*", command):
            logging.info(f"Command matches ChatGPT: {command}")
            return open_chrome_to_chatgpt()
        elif re.search(r"(turn off my pc).*", command):
            logging.info(f"Command matches turn off: {command}")
            return shutdown_pc()
        elif re.search(r"(spotify).*", command):
            logging.info(f"Command matches Spotify: {command}")
            return play_music()
        elif re.search(r"(system diagnostic).*", command):
            logging.info(f"Command matches system diagnostic: {command}")
            return check_system_status()
        else:
            logging.info(f"Unknown command, Sending to Gpt: {command}")
            return get_firekeeper_response(context_manager, command) 
    except Exception as e:
        logging.error(f"Error in processing command '{command}': {str(e)}")
        return "An error occurred while processing your request, Ashen One."

def process_command(command, context_manager):
    return handle_command(command, context_manager)