"""Page Object da página inicial do Kabum."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config.settings import BASE_URL
from pages.base_page import BasePage
from utils import utils


class HomePage(BasePage):
	"""Representa a página inicial do Kabum."""

	LOGO_LOCATOR = (By.CSS_SELECTOR, "img[class='w-[106px] desktop:w-full']")

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
