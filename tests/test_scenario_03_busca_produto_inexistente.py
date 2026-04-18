"""Teste do Cenário 3: busca por produto inexistente."""

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_buscar_produto_inexistente(driver):
	"""Cenário 3: ao buscar item inexistente, não deve haver resultados."""
	home_page = HomePage(driver)
	results_page = SearchResultsPage(driver)
	expected_message = "Lamentamos, nenhum produto encontrado com esse critério de pesquisa."

	home_page.open()
	home_page.search_product("xyzprodutoinexistente123")

	assert results_page.is_empty_result_message_displayed_with_text(expected_message), (
		"A mensagem de lista vazia não foi exibida com o texto esperado."
	)
