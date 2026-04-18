"""Teste do Cenário 1: abrir página inicial e validar logo."""

from pages.home_page import HomePage


def test_abrir_pagina_inicial_e_exibir_logo(driver):
	"""Cenário 1: ao abrir a home, a logo deve ficar visível."""
	home_page = HomePage(driver)

	home_page.open()

	assert home_page.is_logo_visible(), "A logo da página inicial não foi exibida."
