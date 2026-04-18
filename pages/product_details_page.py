"""Page Object da página de detalhes do produto no Kabum."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
	"""Representa a página de detalhes de um produto."""

	PRODUCT_NAME_LOCATOR = (By.XPATH, "//*[@id='main-content']/div[1]/div[1]/div[1]/div[2]/div/h1")
	PRODUCT_PRICE_LOCATOR = (By.XPATH, "//*[@id='main-content']/div[1]/div[1]/div[1]/div[3]/div[3]/h4")

	def is_on_product_details_page(self):
		"""Retorna True quando a URL atual é de uma página de produto."""
		return "/produto/" in self.driver.current_url

	def is_product_name_visible(self):
		"""Retorna True quando o nome do produto está visível."""
		try:
			self.wait_element_visible(self.PRODUCT_NAME_LOCATOR)
			return self.element_exists(self.PRODUCT_NAME_LOCATOR)
		except TimeoutException:
			return False

	def get_product_name(self):
		"""Obtém o nome exibido na página de detalhes do produto."""
		return self.get_element_text(self.PRODUCT_NAME_LOCATOR)

	def product_name_contains(self, expected_word):
		"""Valida se o nome do produto contém a palavra esperada sem case-sensitive."""
		product_name = self.get_product_name()
		return expected_word.lower() in product_name.lower()

	def is_product_price_visible(self):
		"""Retorna True quando o preço do produto está visível."""
		try:
			self.wait_element_visible(self.PRODUCT_PRICE_LOCATOR)
			return self.element_exists(self.PRODUCT_PRICE_LOCATOR)
		except TimeoutException:
			return False

	def get_product_price(self):
		"""Obtém o preço exibido na página de detalhes do produto."""
		return self.get_element_text(self.PRODUCT_PRICE_LOCATOR)

	def product_price_contains(self, expected_text):
		"""Valida se o preço do produto contém o texto esperado."""
		product_price = self.get_product_price()
		return expected_text in product_price
