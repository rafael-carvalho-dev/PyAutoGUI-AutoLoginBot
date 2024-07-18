from dotenv import load_dotenv
from time import sleep
import logging
import os
import pyautogui
import sys
import webbrowser

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL da página de login
URL = 'https://membros.devaprender.com/'

# Caminhos das imagens
EMAIL_FIELD_IMG = 'C:/Users/rafae/Documents/project_site_automation/img/email_field.png'
PASSCODE_FIELD_IMG = 'C:/Users/rafae/Documents/project_site_automation/img/passcode_field.png'
ENTER_BUTTON_IMG = 'C:/Users/rafae/Documents/project_site_automation/img/enter_button.png'

def verify_image_path(image_path):
    """Verifica se o caminho da imagem existe"""
    if not os.path.exists(image_path):
        logging.error(f'Arquivo de imagem não encontrado: {image_path}')
        raise FileNotFoundError(f'Arquivo de imagem não encontrado: {image_path}')
    logging.info(f'Arquivo de imagem encontrado: {image_path}')

def load_credentials():
    """Carrega as credenciais do arquivo .env"""
    load_dotenv()
    user_email = os.getenv('EMAIL_ADDRESS')
    pass_code = os.getenv('PASS_CODE')
    
    if not user_email or not pass_code:
        raise ValueError("Credenciais não encontradas. Verifique o arquivo .env.")
    
    logging.info('Dados de login carregados com sucesso.')
    return user_email, pass_code

def locate_and_click(image_path, confidence=0.8, duration=0.5):
    """Localiza um elemento na tela e clica nele"""
    verify_image_path(image_path)
    element = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    if element is None:
        raise FileNotFoundError(f"Elemento não encontrado: {image_path}")
    pyautogui.click(element, duration=duration)
    sleep(1)

def login(user_email, pass_code):
    """Realiza o processo de login automatizado"""
    try:
        # Localiza e preenche o campo e-mail
        locate_and_click(EMAIL_FIELD_IMG)
        pyautogui.typewrite(user_email, interval=0.2)
        sleep(1)
        
        # Localiza e preenche o campo senha
        locate_and_click(PASSCODE_FIELD_IMG)
        pyautogui.typewrite(pass_code, interval=0.2)
        sleep(1)
        
        # Localiza e clica no botão entrar
        locate_and_click(ENTER_BUTTON_IMG)
        sleep(2)
    
        logging.info('Login efetuado com sucesso.')

    except FileNotFoundError as fnf_error:
        logging.error(f'Erro ao tentar localizar elemento: {fnf_error}')
        sys.exit(1)
    except pyautogui.FailSafeException as fse:
        logging.error(f'Erro de segurança do PyAutoGUI: {fse}')
        sys.exit(1)
    except Exception as e:
        logging.error(f'Erro ao tentar efetuar login: {e}')
        sys.exit(1)

def main():
    """Função principal para abrir navegador, carregar credenciais e efetuar login"""
    try:
        # Abre navegador na URL especificada
        webbrowser.open(URL)
        logging.info(f'Acessando a URL: {URL}')
        sleep(10) # Aguarda carregamento de página
        
        # Carrega as credenciais do arquivo .env
        user_email, pass_code = load_credentials()
        
        # Realiza o login utilizando as credenciais carregadas
        login(user_email, pass_code)
        
    except Exception as e:
        logging.error(f'Erro ao tentar abrir o navegador ou falha ao carregar página: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
