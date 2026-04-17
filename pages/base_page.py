"""
Classe base para todas as páginas - contém métodos comuns
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import WAIT_TIME


class BasePage:
    """
    Classe base que encapsula o driver do Selenium
    Todas as páginas herdam desta classe
    """
    
    def __init__(self, driver):
        """
        Inicializa a página com o driver
        
        Args:
            driver: instância do Selenium WebDriver
        """
        self.driver = driver
    
    def wait_element_visible(self, locator, wait_time=WAIT_TIME):
        """
        Espera um elemento ficar visível na página
        
        Args:
            locator: tupla (By.ID, "id_do_elemento") ou similar
            wait_time: tempo máximo de espera em segundos
        """
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click(self, locator):
        """
        Clica em um elemento
        
        Args:
            locator: tupla (By.ID, "id_do_elemento") ou similar
        """
        element = self.wait_element_visible(locator)
        element.click()
    
    def type_text(self, locator, text):
        """
        Escreve texto em um campo
        
        Args:
            locator: tupla (By.ID, "id_do_elemento") ou similar
            text: texto a ser escrito
        """
        element = self.wait_element_visible(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        """
        Obtém o texto de um elemento
        
        Args:
            locator: tupla (By.ID, "id_do_elemento") ou similar
            
        Returns:
            str: texto do elemento
        """
        element = self.wait_element_visible(locator)
        return element.text
    
    def element_exists(self, locator):
        """
        Verifica se um elemento existe na página
        
        Args:
            locator: tupla (By.ID, "id_do_elemento") ou similar
            
        Returns:
            bool: True se existe, False caso contrário
        """
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0
