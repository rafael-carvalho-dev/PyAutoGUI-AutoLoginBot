from dotenv import load_dotenv
from time import sleep
import logging
import os
import pyautogui
import sys
import webbrowser

# Logger configuration
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Login page URL
URL = 'https://example.com/'

# Image paths
EMAIL_FIELD_IMG = '../images/email_field.png'
PASSWORD_FIELD_IMG = '../images/password_field.png'
ENTER_BUTTON_IMG = '../images/enter_button.png'

def verify_image_path(image_path):
    """
    Check if the image path exists.

    Args:
        image_path (str): Path to the image file.

    Raises:
        FileNotFoundError: If the image file does not exist.
    """
    if not os.path.exists(image_path):
        logging.error(f'Image file not found: {image_path}')
        raise FileNotFoundError(f'Image file not found: {image_path}')
    logging.info(f'Image file found: {image_path}')

def load_credentials():
    """
    Load the credentials from the .env file.

    Returns:
        tuple: A tuple containing the user email and password.

    Raises:
        ValueError: If credentials are not found in the .env file.
    """
    load_dotenv(dotenv_path='../.env')
    user_email = os.getenv('USER_EMAIL')
    password = os.getenv('PASSWORD')
    
    if not user_email or not password:
        raise ValueError("Credentials not found. Check the .env file.")
    
    logging.info('Login data uploaded successfully.')
    return user_email, password

def locate_and_click(image_path, confidence=0.8, duration=0.5):
    """
    Locate an element on the screen and click on it.

    Args:
        image_path (str): Path to the image file.
        confidence (float, optional): Confidence level for image matching. Defaults to 0.8.
        duration (float, optional): Duration of the click action. Defaults to 0.5 seconds.

    Raises:
        FileNotFoundError: If the element is not found on the screen.
    """
    verify_image_path(image_path)
    element = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    if element is None:
        raise FileNotFoundError(f"Element not found: {image_path}")
    pyautogui.click(element, duration=duration)
    sleep(1)

def login(user_email, password):
    """
    Automates the login process.

    Args:
        user_email (str): The user's email address.
        password (str): The user's password.

    Raises:
        SystemExit: If an error occurs during the login process.
    """
    try:
        # Find and fill in the e-mail field
        locate_and_click(EMAIL_FIELD_IMG)
        pyautogui.typewrite(user_email, interval=0.2)
        sleep(1)
        
        # Find and fill in the password field
        locate_and_click(PASSWORD_FIELD_IMG)
        pyautogui.typewrite(password, interval=0.2)
        sleep(1)
        
        # Find and click the enter button
        locate_and_click(ENTER_BUTTON_IMG)
        sleep(2)
    
        logging.info('Login successful.')

    except FileNotFoundError as fnf_error:
        logging.error(f'Error while trying to locate element: {fnf_error}')
        sys.exit(1)
    except pyautogui.FailSafeException as fse:
        logging.error(f'PyAutoGUI security error: {fse}')
        sys.exit(1)
    except Exception as e:
        logging.error(f'Error when trying to log in: {e}')
        sys.exit(1)

def main():
    """
    Main function for opening browser, loading credentials, and logging in.
    
    Raises:
        SystemExit: If an error occurs during the process.
    """
    try:
        # Opens browser at the specified URL
        webbrowser.open(URL)
        logging.info(f'Accessing URL: {URL}')
        sleep(10) # Waiting for page load
        
        # Load credentials from .env file
        user_email, password = load_credentials()
        
        # Logs in using the loaded credentials
        login(user_email, password)
        
    except Exception as e:
        logging.error(f'Error when trying to open browser or failure to load page: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
