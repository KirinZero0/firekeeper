import os
import logging
import time
import threading 
from src.gpt_4o_mini import get_firekeeper_response

def delayed_shutdown():
    """Wait for 5 seconds before shutting down the PC."""
    time.sleep(5)
    system_name = os.name
    try:
        if system_name == 'nt':  # Windows
            os.system("shutdown /s /f /t 0")
        elif system_name == 'posix':  # Linux/Unix
            os.system("shutdown -h now")
        else:
            logging.error("Unsupported OS for shutdown")
    except Exception as e:
        logging.error(f"Error shutting down the PC: {str(e)}")

def shutdown_pc(context_manager, command):
    logging.info("PC shutdown initiated")
    
    system_message = {
        "role": "system",
        "content": "You are the Firekeeper, a mystical guide for Ashen One. Answer with care, as Ashen One is preparing to leave and has requested that their PC be turned off. Keep your responses gentle, but ensure they acknowledge the user's wish to depart and the shutting down of the PC. Keep your response to no more than 3 sentences."
    }
    
    response = get_firekeeper_response(context_manager, command, system_message)
    
    message = "May thou thy peace discover. I shall wait for thy return."
    logging.info(message)
    
    threading.Thread(target=delayed_shutdown).start() 
    
    return response