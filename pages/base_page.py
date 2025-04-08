import allure
from data.urls import Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from data.locators import YaScooterHomePageLocator as Locators

class Base():
    def __init__(self, driver):
        self.driver = driver

    def wait_until_presence_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message= "Не верный локатор для элемента{locator}")
    
    def wait_until_presence_of_all_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),message="Неверный локатор для элементов{locator}")

    def wait_until_element_to_be_clickable(self,locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

class BasePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, locator, time=10):
        return self.wait_until_presence_of_element_located(locator, time)

    def find_elements(self, locator, time=10):
        return self.wait_until_presence_of_all_elements_located(locator, time)
        
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
        return self.wait_until_element_to_be_clickable(Locators.FAQ_BUTTONS)
    
    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url