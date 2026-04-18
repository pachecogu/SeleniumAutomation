"""Page Object da página inicial do Kabum."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config.settings import BASE_URL
from pages.base_page import BasePage
from utils import utils


class HomePage(BasePage):
	"""Representa a página inicial do Kabum."""

	LOGO_LOCATOR = (By.CSS_SELECTOR, "img[class='w-[106px] desktop:w-full']")
	INITIAL_POPUP_TEXT_LOCATOR = (By.CSS_SELECTOR, "#editable-text-1573815308030")
	INITIAL_POPUP_CLOSE_LOCATOR = (By.CSS_SELECTOR, "#close-button-1573815308034 > span")
	SEARCH_INPUT_LOCATOR = (By.ID, "inputBusca")
	SEARCH_BUTTON_LOCATOR = (
		By.CSS_SELECTOR,
		"button[data-testid='buttonBuscaKabum']",
	)
	HARDWARE_MENU_BUTTON_LOCATOR = (By.CSS_SELECTOR, "a[aria-label='Botão do menu (Hardware)']")

	def open(self):
		"""Abre a URL base do Kabum."""
		utils.goto(self.driver, BASE_URL)
		self.close_initial_popup_if_visible()

	def close_initial_popup_if_visible(self):
		"""Fecha o pop-up inicial quando ele estiver visível na home."""
		try:
			self.wait_element_visible(self.INITIAL_POPUP_TEXT_LOCATOR, wait_time=2)
			close_button = self.wait_element_visible(self.INITIAL_POPUP_CLOSE_LOCATOR, wait_time=2)
			self.driver.execute_script("arguments[0].click();", close_button)
		except TimeoutException:
			# Quando o pop-up não existir, o fluxo segue normalmente.
			pass

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

	def click_hardware_menu_button(self):
		"""Clica no botão do menu de Hardware na home."""
		hardware_button = self.wait_element_visible(self.HARDWARE_MENU_BUTTON_LOCATOR)
		self.driver.execute_script(
			"arguments[0].scrollIntoView({block: 'center'});",
			hardware_button,
		)
		self.driver.execute_script("arguments[0].click();", hardware_button)
