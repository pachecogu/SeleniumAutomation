# SeleniumAutomation

## Padrão de projeto utilizado

Este projeto utiliza o padrão Page Object Model (POM).

No POM, cada página do site é representada por uma classe na pasta pages. 
Os elementos e ações da página ficam nessa classe, e os testes na pasta tests apenas chamam esses métodos.
Assim, a automação fica organizada e fácil de manter.

## Como instalar o projeto

Pré-requisitos:

- Python 3.11+
- Google Chrome instalado

1. Acesse a pasta do projeto:

-->powershell
cd C:\PUC\Projects\SeleniumAutomation


2. Crie o ambiente virtual (primeira execução):

-->powershell
python -m venv .venv


3. Ative o ambiente virtual:

-->powershell
.\.venv\Scripts\Activate.ps1


4. Instale as dependências:

-->powershell
python -m pip install -r requirements.txt


No Git Bash, os comandos equivalentes são:

-->bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt


## Como executar e verificar os logs

Para executar os testes:

-->bash
python -m pytest


Para verificar os logs no terminal com mais detalhes:

-->bash
python -m pytest -v -s --log-cli-level=INFO


Para salvar os logs em arquivo:

-->powershell
python -m pytest -v *> logs_execucao.txt


Para salvar os logs em arquivo no Git Bash:

-->bash
python -m pytest -v > logs_execucao.txt 2>&1

