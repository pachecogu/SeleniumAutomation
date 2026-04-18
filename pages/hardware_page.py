"""Page Object da página de Hardware no Kabum."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HardwarePage(BasePage):
	"""Representa a página/campanha de Hardware."""

	HARDWARE_PAGE_URL_PART = "/promocao/HARDWAREKABUM"
	PAGE_MAIN_BANNER_LOCATOR = (By.CSS_SELECTOR, "img[alt='Hardware']")

	def is_on_hardware_page(self):
		"""Retorna True quando a URL atual corresponde à página de Hardware."""
		return self.HARDWARE_PAGE_URL_PART in self.driver.current_url
