"""Teste do Cenário 5: navegar para a categoria PC Gamer."""

from pages.hardware_page import HardwarePage
from pages.home_page import HomePage


def test_navegar_para_categoria_pc_gamer(driver):
	"""Cenário 5: abrir a home, clicar no menu Hardware e validar página."""
	home_page = HomePage(driver)
	hardware_page = HardwarePage(driver)

	home_page.open()
	home_page.click_hardware_menu_button()

	assert hardware_page.is_on_hardware_page(), (
		"A navegação para a página de Hardware não aconteceu."
	)




