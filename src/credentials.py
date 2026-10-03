import logging
import os
from dotenv import load_dotenv
from src.config import ENV_FILE

def load_credentials():
    """
    Load credentials from the .env file.
    """
    
    load_dotenv(dotenv_path=ENV_FILE)
    
    user_email = os.getenv("USER_EMAIL")
    password = os.getenv("PASSWORD")
    
    if not user_email or not password:
        raise ValueError(
            "Credential not found. Check the .env file."
        )
        
    logging.info("Credential loaded successfully.")
    
    return user_email, password