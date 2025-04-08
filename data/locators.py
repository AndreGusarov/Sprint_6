from selenium.webdriver.common.by import By


class BasePageLocator:
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    YANDEX_SITE_BUTTON = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
    SCOOTER_SITE_BUTTON = [By.XPATH, ".//img[@alt='Scooter']"]


class YaScooterHomePageLocator:
    TOP_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    FAQ_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]

    @staticmethod
    def FAQ_ANSWER(answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]


class YaScooterOrderPageLocator:
    FIRST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    LAST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    ADDRESS_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    SUBWAY_FIELD = [By.XPATH, ".//input[contains(@placeholder,'метро')]"] 


    @staticmethod
    def SUBWAY_HINT_BUTTON(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]
       
    PHONE_NUMBER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]

    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    DATE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    COMMENT_FOR_COURIER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_COMPLETED_INFO = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    SHOW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]
