import logging
import psutil

def check_system_status():
    try:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        status = f"Ah, Ashen One... Your CPU Usage is {cpu}%, and the Memory Usage is {memory}%. Take care of your machine, for it too needs rest."
        logging.info("Checked system status")
        return status
    except ImportError:
        logging.error("psutil module not found, cannot check system status")
        return "I am unable to check your system's health, Ashen One... It seems the psutil module is missing."
