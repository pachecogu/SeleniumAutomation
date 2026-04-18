"""Teste do Cenário 4: visualizar detalhes do primeiro produto."""

from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage


def test_acessar_pagina_de_detalhes_do_primeiro_produto(driver):
	"""Cenário 4: ao clicar no primeiro resultado, deve exibir nome e preço do produto."""
	home_page = HomePage(driver)
	results_page = SearchResultsPage(driver)
	product_details_page = ProductDetailsPage(driver)

	home_page.open()
	home_page.search_product("notebook")

	assert results_page.is_product_list_displayed(), "A lista de produtos não foi exibida."

	results_page.open_first_product_details()

	assert product_details_page.is_on_product_details_page(), (
		"A navegação para a página de detalhes do produto não aconteceu."
	)
	assert product_details_page.is_product_name_visible(), "O nome do produto não ficou visível."
	assert product_details_page.product_name_contains("notebook"), (
		"O nome do produto não contém a palavra 'notebook'."
	)
	assert product_details_page.is_product_price_visible(), "O preço do produto não ficou visível."
	assert product_details_page.product_price_contains("R$"), (
		"O preço do produto não contém 'R$'."
	)
