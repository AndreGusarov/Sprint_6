import allure
from data.urls import Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message= "Не верный локатор для элемента{locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),message="Неверный локатор для элементов{locator}")
    
    def go_to_site(self, url=None):
        if url is None:
            url = Url.MAIN_PAGE
            self.driver.get(url)
    
    def go_to_order(self, url=None):
        if url is None:
            url = Url.ORDER_PAGE
            self.driver.get(url)

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    
    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url