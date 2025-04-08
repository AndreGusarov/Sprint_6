import allure
from pages.base_page import BasePage
from data.locators import YaScooterOrderPageLocator as Locators
import re

class YaScooterOrderPage(BasePage):
    @allure.step('Ввод имени')
    def input_first_name(self, first_name):
        return self.find_element(Locators.FIRST_NAME_INPUT).send_keys(first_name)
    
    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name):
        return self.find_element(Locators.LAST_NAME_INPUT).send_keys(last_name)
    
    @allure.step('Ввод адреса')
    def input_address(self, address):
        return self.find_element(Locators.ADDRESS_INPUT).send_keys(address)
    
    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        self.find_element(Locators.SUBWAY_FIELD).click()
        return self.find_element(Locators.SUBWAY_HINT_BUTTON(subway_name)).click()

    
    @allure.step('Ввод номера телефона')
    def input_phone_number(self, phone_number):
        return self.find_element(Locators.PHONE_NUMBER_FIELD).send_keys(phone_number)
    
    @allure.step('Переход на следующую страницу заказа')
    def got_next(self):
        return self.find_element(Locators.NEXT_BUTTON).click()
    
    @allure.step('Ввод даты')
    def input_date(self, date):
        return self.find_element(Locators.DATE_FIELD).send_keys(date)
    
    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option):
        self.find_element(Locators.RENTAL_PERIOD_FIELD).click()
        return self.find_elements(Locators.RENTAL_PERIOD_LIST)[option].click()
    
    @allure.step('Выбор цвета')
    def choose_color(self, option):
        if isinstance(option, list):
            for option in option:
                self.find_elements(Locators.COLOR_CHECKBOXES)[option].click()
        else:
            self.find_elements(Locators.COLOR_CHECKBOXES)[option].click()
    
    @allure.step('Комментарий курьеру')
    def input_comment(self, comment_text):
        return self.find_element(Locators.COMMENT_FOR_COURIER_FIELD).send_keys(comment_text)
    
    @allure.step('Нажатие кнопки Заказать')
    def click_order(self):
        return self.find_element(Locators.ORDER_BUTTON).click()
    
    @allure.step('Подтверждение заказа')
    def click_accept_order(self):
        return self.find_element(Locators.ACCEPT_ORDER_BUTTON).click()

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        about_order_text = self.find_element(Locators.ORDER_COMPLETED_INFO).text
        return ''.join(re.findall('[0-9]', about_order_text))
    
    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        return self.find_element(Locators.SHOW_STATUS_BUTTON).click()
    
    @allure.step('Заполнить первую страницу заказа')
    def fill_user_data(self, data_set:dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_phone_number(data_set['phone_number'])

    @allure.step('Заполнить вторую страницу заказа')
    def fill_rent_data(self, data_set:dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        self.choose_color(data_set['color'])
        self.input_comment(data_set['comment_for_courier'])

    
    
    

    