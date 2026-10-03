# Automação de Login com Python e PyAutoGUI

Automação simples de login utilizando Python e PyAutoGUI.

Este projeto foi desenvolvido como um exercício de estudo de automação de tarefas com Python. A aplicação abre uma página web, localiza visualmente os campos de login na tela, preenche as credenciais e realiza o envio do formulário.

> **Aviso:** este projeto é destinado a fins educacionais. Não utilize automações desse tipo em sistemas sem autorização.

**Idiomas**: Português (Brasil)| [English](README.en.md)

## Tecnologias utilizadas

* Python 3
* PyAutoGUI
* python-dotenv

Bibliotecas da biblioteca padrão do Python utilizadas no projeto:

* `pathlib`
* `logging`
* `os`
* `sys`
* `time`
* `webbrowser`

## Funcionalidades

* Abre automaticamente a URL configurada.
* Carrega credenciais a partir de um arquivo `.env`.
* Localiza os elementos da página utilizando reconhecimento de imagem.
* Preenche o campo de e-mail.
* Preenche o campo de senha.
* Localiza e clica no botão de login.
* Registra informações e erros em arquivo de log.
* Utiliza tratamento de exceções para situações inesperadas.

## Estrutura do projeto

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

## Pré-requisitos

É necessário ter o Python 3 instalado.

Recomenda-se utilizar um ambiente virtual (`venv`) para isolar as dependências do projeto.

### Verificar a instalação do Python

Windows:

```powershell
py --version
```

Linux/macOS:

```bash
python3 --version
```

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre no diretório:

```bash
cd login-automation
```

### Windows PowerShell

Crie o ambiente virtual:

```powershell
py -m venv .venv
```

Ative:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Linux/macOS

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto.

Você pode utilizar o `.env.example` como referência:

```env
USER_EMAIL=your_email@example.com
PASSWORD=your_password
```

Substitua os valores pelos dados necessários para a execução do projeto.

**Nunca envie o arquivo `.env` para o GitHub.**

O arquivo `.env` está incluído no `.gitignore` justamente para evitar o versionamento de credenciais.

## Imagens utilizadas pela automação

O PyAutoGUI utiliza imagens como referência para localizar os elementos na tela.

As imagens esperadas são:

```text
images/
├── email_field.png
├── password_field.png
└── enter_button.png
```

Essas imagens devem corresponder visualmente aos elementos presentes na página que será automatizada.

Alterações no layout, resolução, escala da tela, tema do navegador ou aparência dos elementos podem afetar o reconhecimento das imagens.

## Execução

Com o ambiente virtual ativado, execute:

```bash
python -m src.main
```

O programa irá:

1. Abrir a URL configurada.
2. Carregar as credenciais do `.env`.
3. Procurar o campo de e-mail.
4. Preencher o e-mail.
5. Procurar o campo de senha.
6. Preencher a senha.
7. Procurar o botão de login.
8. Clicar no botão.
9. Registrar informações da execução no log.

## Logs

As informações de execução são registradas em:

```text
logs/app.log
```

O diretório `logs/` não deve ser versionado.

## Limitações

Por utilizar reconhecimento de imagem e interação com a interface gráfica, a automação depende das condições da tela.

Por exemplo:

* resolução do monitor;
* escala de exibição;
* posição da janela;
* aparência dos elementos;
* carregamento da página;
* alterações no layout do site;
* tema claro ou escuro;
* disponibilidade dos elementos na tela.

Por isso, a automação pode exigir ajustes caso o ambiente seja alterado.

## Possíveis melhorias

Algumas melhorias que podem ser implementadas futuramente:

* substituir esperas fixas por esperas condicionais;
* validar se o login realmente foi concluído;
* adicionar screenshots em caso de erro;
* melhorar o tratamento de diferentes tipos de falha;
* utilizar seletores HTML com Selenium ou Playwright;
* adicionar testes automatizados para as funções que não dependem da interface gráfica;
* utilizar configurações externas para diferentes ambientes;
* adicionar uma interface de linha de comando.

## Objetivo do projeto

O objetivo principal deste projeto é estudar conceitos de:

* Python;
* modularização;
* funções;
* tratamento de exceções;
* gerenciamento de dependências;
* ambientes virtuais;
* variáveis de ambiente;
* logging;
* automação de interface gráfica;
* organização de projetos Python.

## Licença

Este projeto pode ser utilizado para fins de estudo.

## Autor

Rafael Carvalho Álvares da Silva

* GitHub: `https://github.com/rafael-carvalho-dev/`
* LinkedIn: `<LINKEDIN_PROFILE_URL>`