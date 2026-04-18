"""Teste do Cenário 2: busca por produto existente."""

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_buscar_produto_existente(driver):
	"""Cenário 2: ao buscar notebook, deve exibir lista e o primeiro nome conter notebook."""
	home_page = HomePage(driver)
	results_page = SearchResultsPage(driver)

	home_page.open()
	home_page.search_product("notebook")

	assert results_page.is_product_list_displayed(), "A lista de produtos não foi exibida."
	assert results_page.first_product_contains("notebook"), (
		"O primeiro produto não contém a palavra 'notebook' no nome."
	)
