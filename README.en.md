# Login Automation with Python and PyAutoGUI

Simple login automation using Python and PyAutoGUI.

This project was developed as a learning exercise focused on task automation with Python. The application opens a web page, visually locates the login fields on the screen, enters the credentials, and submits the login form.

> **Disclaimer:** this project is intended for educational purposes. Do not use this type of automation on systems without proper authorization.

**Languages:** [Português (Brasil)](README.md) | English

## Technologies

* Python 3
* PyAutoGUI
* python-dotenv

Python standard library modules used by the project:

* `pathlib`
* `logging`
* `os`
* `sys`
* `time`
* `webbrowser`

## Features

* Automatically opens the configured URL.
* Loads credentials from a `.env` file.
* Locates page elements using image recognition.
* Fills in the email field.
* Fills in the password field.
* Locates and clicks the login button.
* Records information and errors in a log file.
* Handles unexpected errors through exception handling.

## Project structure

```text
login-automation/
│
├── .env.example
├── .gitignore
├── README.md
├── README.en.md
├── requirements.txt
│
├── images/
│   ├── email_field.png
│   ├── password_field.png
│   └── enter_button.png
│
├── logs/
│
└── src/
    ├── __init__.py
    ├── main.py
    ├── config.py
    ├── credentials.py
    ├── screen.py
    └── login.py
```

## Requirements

Python 3 must be installed.

Using a virtual environment (`venv`) is recommended to isolate the project's dependencies.

### Check the Python installation

Windows:

```powershell
py --version
```

Linux/macOS:

```bash
python3 --version
```

## Installation

Clone the repository:

```bash
git clone <REPOSITORY_URL>
```

Enter the project directory:

```bash
cd login-automation
```

### Windows PowerShell

Create the virtual environment:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Linux/macOS

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root.

You can use `.env.example` as a reference:

```env
USER_EMAIL=your_email@example.com
PASSWORD=your_password
```

Replace the values with the credentials required to run the project.

**Never commit the `.env` file to GitHub.**

The `.env` file is included in `.gitignore` to prevent credentials from being committed to the repository.

## Images used by the automation

PyAutoGUI uses images as references to locate elements on the screen.

The following images are expected:

```text
images/
├── email_field.png
├── password_field.png
└── enter_button.png
```

These images must visually match the elements displayed on the page being automated.

Changes to the layout, screen resolution, display scaling, browser theme, or element appearance may affect image recognition.

## Running the project

With the virtual environment activated, run:

```bash
python -m src.main
```

The application will:

1. Open the configured URL.
2. Load the credentials from `.env`.
3. Search for the email field.
4. Enter the email.
5. Search for the password field.
6. Enter the password.
7. Search for the login button.
8. Click the button.
9. Record execution information in the log.

## Logs

Execution information is stored in:

```text
logs/app.log
```

The `logs/` directory should not be committed to the repository.

## Limitations

Because the automation relies on image recognition and graphical user interface interaction, it depends on the conditions of the screen.

For example:

* monitor resolution;
* display scaling;
* window position;
* element appearance;
* page loading time;
* changes to the website layout;
* light or dark themes;
* availability of elements on the screen.

Therefore, the automation may require adjustments when the environment changes.

## Possible improvements

Future improvements may include:

* replacing fixed delays with conditional waits;
* verifying that the login was actually successful;
* taking screenshots when an error occurs;
* improving handling of different failure scenarios;
* using HTML selectors with Selenium or Playwright;
* adding automated tests for functions that do not depend on the graphical interface;
* using external configuration for different environments;
* adding a command-line interface.

## Project purpose

The main purpose of this project is to study:

* Python;
* modularization;
* functions;
* exception handling;
* dependency management;
* virtual environments;
* environment variables;
* logging;
* graphical user interface automation;
* Python project organization.

## License

This project may be used for learning purposes.

## Author

Rafael Carvalho Álvares da Silva

* GitHub: `https://github.com/rafael-carvalho-dev/`
* LinkedIn: `<LINKEDIN_PROFILE_URL>`