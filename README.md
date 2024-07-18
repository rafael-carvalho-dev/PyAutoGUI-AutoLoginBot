# login-automation-bot
# Login Automation Bot

This project is a Python-based automation script designed to perform automated login tasks on a specified website using PyAutoGUI. The bot opens a web browser, navigates to the login page, inputs the user credentials, and logs in automatically. 

## Features

- **Automated Login**: Automatically fills in email and password fields and submits the login form.
- **Environment Variables**: Uses environment variables to securely manage login credentials.
- **Image Recognition**: Utilizes PyAutoGUI to locate and interact with UI elements based on screenshots.
- **Error Handling**: Robust error handling and logging to track the script's execution.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/login-automation-bot.git
    cd login-automation-bot
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory and add your login credentials:
    ```sh
    EMAIL_ADDRESS=your_email@example.com
    PASS_CODE=your_password
    ```

4. Update the paths to the image files in the script if necessary.

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. The script will open a web browser, navigate to the login page, and perform the login operation using the credentials provided in the `.env` file.

## Configuration

Ensure the paths to the image files used for locating the email field, password field, and login button are correctly set in the script:

```python
EMAIL_FIELD_IMG = 'path/to/email_field.png'
PASSCODE_FIELD_IMG = 'path/to/passcode_field.png'
ENTER_BUTTON_IMG = 'path/to/enter_button.png'
```

## Logging
The script includes logging functionality to track its operations. Logs are displayed in the console, providing information about the script's progress and any errors encountered.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

This automation script is intended for educational purposes and personal use. Please ensure you have permission to automate the login process for any website you use this script with.


### How to Use the README
1. **Title**: The title should clearly describe the purpose of the repository.
2. **Features**: Highlight the main features of the project.
3. **Prerequisites**: List the required software and dependencies.
4. **Installation**: Provide step-by-step instructions to set up the project.
5. **Usage**: Explain how to run the script.
6. **Configuration**: Guide the user to configure the script correctly.
7. **Logging**: Mention the logging functionality.
8. **Contributing**: Encourage contributions and provide guidelines.
9. **License**: Specify the license under which the project is distributed.

This README provides a comprehensive overview of the project, helping users understand its purpose, set it up, and use it effectively.

