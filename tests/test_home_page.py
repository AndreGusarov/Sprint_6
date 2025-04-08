import pytest
import allure
from data.urls import Url
from pages.home_page import YaScooterHomePage

@allure.epic('Main page')
@allure.parent_suite('Main page navigation tests')
@allure.suite('Navigation suite')
class TestYaScooterHomePage:
    @allure.feature('Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Переход к оформлению заказа по кнопке по верхней кнопке "Заказать"')
    @allure.title('Нажатие на кнопку "Заказать" в хедере')
    @allure.description('Проверка, что при нажатии по кнопке "Заказать", просходит переход на страницу оформления заказа')
    def test_click_top_order_button_navigates_to_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookies_accept()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Url.ORDER_PAGE

    @allure.feature('Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Переход к оформлению заказа по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Нажатие на кнопку "Заказать", в блоке "Как это работает".')
    @allure.description('Проверка, что при нажатии по кнопке "Заказать", просходит переход на страницу оформления заказа')
    def test_click_bottom_order_button_navigates_to_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookies_accept()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Url.ORDER_PAGE     

    @allure.feature('Переход на главную страницу ЯндексСамокат')
    @allure.story('Переход на страницу ЯндексСамокат по кнопке лого в хедере')
    @allure.title('При нажатии на лого "ЯндексСамокат" переход на главную страницу"')
    @allure.description('Проверка перехода по кнопке "ЯндексСамокат" на главную страницу')
    def test_click_scooter_logo_navigates_to_main_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_order()
        ya_scooter_home_page.click_cookies_accept()
        ya_scooter_home_page.click_yandex_scooter_button()

        assert ya_scooter_home_page.current_url().rstrip('/') == Url.BASE_URL

    @allure.feature('Переход на страницу "ЯндексДзен" с Домашней страницы')
    @allure.story('Переход на страницу ЯндексДзен по кнопке лого в хедере')
    @allure.title('При нажатии на лого "Яндекс" переход на страницу "ЯндексДзен"')
    @allure.description('Проверка перехода по кнопке "Яндекс" на страницу "ЯндексДзен"')
    def test_click_yandex_logo_navigates_to_yandex_dzen(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookies_accept()
        ya_scooter_home_page.click_yandex_button()
        ya_scooter_home_page.switch_window(1)
        ya_scooter_home_page.wait_untill_about_blank_dissappear()
        current_url = ya_scooter_home_page.current_url()

        assert (Url.YANDEX_DZEN in current_url) or (Url.YANDEX_HOME_PAGE)