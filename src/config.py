from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

IMAGES_DIR = BASE_DIR / "images"
LOGS_DIR = BASE_DIR / "logs"

EMAIL_FIELD_IMG = IMAGES_DIR / "email_field.png"
PASSWORD_FIELD_IMG = IMAGES_DIR / "password_field.png"
ENTER_BUTTON_IMG = IMAGES_DIR / "enter_button.png"

URL = "https://example.com"