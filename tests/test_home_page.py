"""Testes da página inicial do Kabum."""

from pages.home_page import HomePage


def test_abrir_pagina_inicial_e_exibir_logo(driver):
	"""Cenário 1: ao abrir a home, a logo deve ficar visível."""
	home_page = HomePage(driver)

	home_page.open()

	assert home_page.is_logo_visible(), "A logo da página inicial não foi exibida."


def test_buscar_produto_existente(driver):
	"""Cenário 2: ao buscar notebook, deve exibir lista e o primeiro nome conter notebook."""
	home_page = HomePage(driver)

	home_page.open()
	home_page.search_product("notebook")

	assert home_page.is_product_list_displayed(), "A lista de produtos não foi exibida."
	assert home_page.first_product_contains("notebook"), (
		"O primeiro produto não contém a palavra 'notebook' no nome."
	)


def test_buscar_produto_inexistente(driver):
	"""Cenário 3: ao buscar item inexistente, não deve haver resultados."""
	home_page = HomePage(driver)
	expected_message = "Lamentamos, nenhum produto encontrado com esse critério de pesquisa."

	home_page.open()
	home_page.search_product("xyzprodutoinexistente123")

	assert home_page.is_empty_result_message_displayed_with_text(expected_message), (
		"A mensagem de lista vazia não foi exibida com o texto esperado."
	)
