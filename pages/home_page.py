"""Page Object da página inicial do Kabum."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config.settings import BASE_URL
from pages.base_page import BasePage
from utils import utils


class HomePage(BasePage):
	"""Representa a página inicial do Kabum."""

	LOGO_LOCATOR = (By.CSS_SELECTOR, "img[class='w-[106px] desktop:w-full']")
	SEARCH_INPUT_LOCATOR = (By.ID, "inputBusca")
	SEARCH_BUTTON_LOCATOR = (
		By.CSS_SELECTOR,
		"button[data-testid='buttonBuscaKabum']",
	)
	PRODUCT_CARDS_LOCATOR = (
		By.CSS_SELECTOR,
		"main a[href*='/produto/']:first-of-type > span",
	)
	EMPTY_RESULT_MESSAGE_LOCATOR = (By.XPATH, "//*[@id='listingEmpty']/b")

	def open(self):
		"""Abre a URL base do Kabum."""
		utils.goto(self.driver, BASE_URL)

	def is_logo_visible(self):
		"""Retorna True quando a logo da home está visível."""
		try:
			self.wait_element_visible(self.LOGO_LOCATOR)
			return True
		except TimeoutException:
			return False

	def fill_search_input(self, search_text):
		"""Preenche o campo de busca com o texto informado."""
		self.type_text(self.SEARCH_INPUT_LOCATOR, search_text)

	def click_search_button(self):
		"""Clica no botão de busca."""
		self.click(self.SEARCH_BUTTON_LOCATOR)

	def search_product(self, search_text):
		"""Executa a busca por um produto na home."""
		self.fill_search_input(search_text)
		self.click_search_button()

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

	def has_search_results(self):
		"""Retorna True quando a busca possui ao menos um resultado visível."""
		try:
			self.wait_element_visible(self.PRODUCT_CARDS_LOCATOR)
			return self.element_exists(self.PRODUCT_CARDS_LOCATOR)
		except TimeoutException:
			return False

	def has_no_search_results(self):
		"""Retorna True quando a busca não exibe resultados."""
		return not self.has_search_results()

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
