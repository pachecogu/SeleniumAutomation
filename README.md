# SeleniumAutomation

Projeto simples de automação com Python + Selenium + pytest, usando Page Object Model (POM).

## Pré-requisitos

- Python 3.11+
- Google Chrome instalado

## Estrutura

- config/: configurações globais
- pages/: Page Objects
- tests/: testes e fixtures
- utils/: utilitários compartilhados

## Setup (PowerShell)

1. Ir para a raiz do projeto:

```powershell
cd C:\PUC\Projects\SeleniumAutomation
```

2. Criar ambiente virtual (apenas na primeira vez):

```powershell
python -m venv .venv
```

3. Ativar ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Instalar dependências:

```powershell
python -m pip install -r requirements.txt
```

## Setup (Git Bash)

1. Ir para a raiz do projeto:

```bash
cd /c/PUC/Projects/SeleniumAutomation
```

2. Ativar ambiente virtual:

```bash
source .venv/Scripts/activate
```

Se você estiver dentro da pasta tests, use:

```bash
source ../.venv/Scripts/activate
```

## Executar os testes

Rodar todos os testes:

```bash
python -m pytest
```

Rodar apenas o cenário da home:

```bash
python -m pytest tests/test_home_page.py -v
```
