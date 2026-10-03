import logging
import pyautogui

from src.config import (
    EMAIL_FIELD_IMG,
    PASSWORD_FIELD_IMG,
    ENTER_BUTTON_IMG
)

from src.screen import locate_and_click

def login(user_email, password):
    """Perform the login process.

    Args:
        user_email (_type_): _description_
        password (_type_): _description_
    """
    
    logging.info("Starting login process.")
    
    locate_and_click(EMAIL_FIELD_IMG)
    pyautogui.write(user_email, interval=0.05)
    
    locate_and_click(PASSWORD_FIELD_IMG)
    pyautogui.write(password, interval=0.05)
    
    locate_and_click(ENTER_BUTTON_IMG)
    
    logging.info("Login process completed.")