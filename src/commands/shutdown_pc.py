import os
import logging

def shutdown_pc():
    logging.info("PC shutdown initiated")
    system_name = os.name
    try:
        if system_name == 'nt':
            os.system("shutdown /s /f /t 0")
        elif system_name == 'posix':
            os.system("shutdown -h now")
        else:
            logging.error("Unsupported OS for shutdown")
            return "Ah, Ashen One... I could not determine your system's nature to carry out the shutdown."

        return "May thou thy peace discover. I shall wait for thy return, ."

    except Exception as e:
        logging.error(f"Error shutting down the PC: {str(e)}")
        return "An error occurred while shutting down your PC, Ashen One... It seems we are not yet ready for rest."
