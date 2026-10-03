import logging
from time import sleep, time
import pyautogui

def verify_image_path(image_path):
    """Verify that an image file exists.

    Args:
        image_path (_type_): _description_
    """
    
    if not image_path.exists():
        raise FileNotFoundError(
            f"Image file not found: {image_path}"
        )
        
def locate_element(image_path, confidence=0.8, timeout=15):
    """Wait until an image is found on the screen.

    Args:
        image_path (_type_): _description_
        confidence (float, optional): _description_. Defaults to 0.8.
        timeout (int, optional): _description_. Defaults to 15.
    """
    
    verify_image_path(image_path)
    
    start_time = time()
    
    logging.info(
        f"Searching for element: {image_path.name}"
    )
    
    while time() - start_time < timeout:
        element = pyautogui.locateCenterOnScreen(
            str(image_path),
            confidence=confidence
        )
        
        if element is not None:
            logging.info(
                f"Element found: {image_path.name}"
            )
            return element
        
        sleep(0.5)
    
    raise TimeoutError(
        f"Element not found within {timeout}s: {image_path}"
    )
    
def locate_and_click(image_path, confidence=0.8, timeout=15):
    """Locate an image on the screen and click it.

    Args:
        image_path (_type_): _description_
        confidence (float, optional): _description_. Defaults to 0.8.
        timeout (int, optional): _description_. Defaults to 15.
    """
    
    element = locate_element(
        image_path=image_path,
        confidence=confidence,
        timeout=timeout
    )
    
    pyautogui.click(element)
    
    sleep(0.5)