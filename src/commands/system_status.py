import logging
import psutil
from src.gpt_4o_mini import get_firekeeper_response

def check_system_status(context_manager, command):
    try:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        system_message = {
            "role": "system",
            "content": f"You are the Firekeeper, a mystical guide for Ashen One. Answer with care. Answer like the Firekeeper from Dark Souls 3. Mention their system health, noting the CPU Usage of {cpu}% and Memory Usage of {memory}%. Let them know their machine is in need of rest, but should continue on their path. Keep your response to no more than 3 sentences."
        }
        response = get_firekeeper_response(context_manager, command, system_message)
        logging.info("Checked system status")
        return response
    except ImportError:
        logging.error("psutil module not found, cannot check system status")
        return "I am unable to check your system's health, Ashen One... It seems the psutil module is missing."
