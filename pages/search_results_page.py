"""Page Object da página de resultados de busca do Kabum."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
	"""Representa a listagem de produtos após uma busca."""

	PRODUCT_CARDS_LOCATOR = (
		By.CSS_SELECTOR,
		"main a[href*='/produto/']:first-of-type > span",
	)
	EMPTY_RESULT_MESSAGE_LOCATOR = (By.XPATH, "//*[@id='listingEmpty']/b")

	def is_product_list_displayed(self):
		"""Retorna True quando existe pelo menos um resultado exibido."""
		try:
			self.wait_element_visible(self.PRODUCT_CARDS_LOCATOR)
			return self.element_exists(self.PRODUCT_CARDS_LOCATOR)
		except TimeoutException:
			return False

	def get_first_product_name(self):
		"""Obtém o nome do primeiro produto listado."""
		return self.get_element_text(self.PRODUCT_CARDS_LOCATOR)

	def first_product_contains(self, expected_word):
		"""Valida se o primeiro produto contém a palavra esperada."""
		first_product_name = self.get_first_product_name()
		return expected_word.lower() in first_product_name.lower()

	def open_first_product_details(self):
		"""Clica no primeiro produto da listagem para abrir a página de detalhes."""
		product_element = self.wait_element_visible(self.PRODUCT_CARDS_LOCATOR)
		self.driver.execute_script(
			"arguments[0].scrollIntoView({block: 'center'});",
			product_element,
		)
		self.driver.execute_script("arguments[0].click();", product_element)

	def get_empty_result_message_text(self):
		"""Obtém o texto da mensagem de busca sem resultados."""
		return self.get_element_text(self.EMPTY_RESULT_MESSAGE_LOCATOR)

	def is_empty_result_message_displayed_with_text(self, expected_text):
		"""Valida se a mensagem de lista vazia existe e possui o texto esperado."""
		try:
			message_text = self.get_empty_result_message_text().strip()
			return message_text == expected_text
		except TimeoutException:
			return False
