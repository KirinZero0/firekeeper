import os
import logging
import time
import threading 

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

def shutdown_pc():
    logging.info("PC shutdown initiated")
    message = "May thou thy peace discover. I shall wait for thy return."
    logging.info(message)
    threading.Thread(target=delayed_shutdown).start() 
    return message