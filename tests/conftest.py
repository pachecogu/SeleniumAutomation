"""Fixtures globais do pytest."""

from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import utils


@pytest.fixture
def driver():
	"""Inicializa e finaliza o navegador para cada teste."""
	options = Options()
	options.add_argument("--start-maximized")
	options.add_argument("--disable-gpu")
	options.add_argument("--disable-dev-shm-usage")

	driver_path = ChromeDriverManager().install()

	# Em algumas versões no Windows, o manager pode retornar o arquivo de notices.
	if driver_path.lower().endswith("third_party_notices.chromedriver"):
		driver_path = str(Path(driver_path).with_name("chromedriver.exe"))

	service = Service(driver_path)
	web_driver = webdriver.Chrome(service=service, options=options)
	yield web_driver
	utils.quit(web_driver)
