"""Teste do Cenário 5: navegar para a categoria PC Gamer."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage


def test_navegar_para_categoria_pc_gamer(driver):
	"""Cenário 5: abrir a home, clicar no menu Hardware e validar URL."""
	home_page = HomePage(driver)
	expected_url = "https://www.kabum.com.br/promocao/HARDWAREKABUM"

	home_page.open()
	home_page.click_hardware_menu_button()

	WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
	assert driver.current_url == expected_url, (
		"A URL atual nao corresponde a https://www.kabum.com.br/promocao/HARDWAREKABUM."
	)





