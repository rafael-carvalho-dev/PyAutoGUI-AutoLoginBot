import logging
import sys
import webbrowser
import pyautogui

from src.config import LOGS_DIR, URL
from src.credentials import load_credentials
from src.login import login

LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / "app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def main():
    try:
        logging.info("Application started.")
        
        webbrowser.open(URL)
        
        user_email, password = load_credentials()
        
        login(user_email, password)
        
        logging.info("Application finished successfully.")
        
    except pyautogui.FailSafeException:
        logging.exception("PyAutoGui fail-safe triggered.")
        sys.exit(1)
        
    except Exception:
        logging.exception("Unexpected application error.")
        sys.exit(1)
        
if __name__ == "__main__":
    main()