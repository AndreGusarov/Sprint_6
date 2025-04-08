import pytest
import allure
from data.urls import Url
from pages.home_page import YaScooterHomePage
from pages.order_page import YaScooterOrderPage
from data.test_data import YaScooterOrderPageData as order_data

@allure.epic('Order')
@allure.parent_suite('Create new order tests')
@allure.suite('Order creation suite')
class TestYaScooterOrderPage:
    @allure.feature('Создание заказа')
    @allure.story('Оформление заказа и просмотр страницы заказа')
    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа" ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_order()
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.click_cookies_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.got_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        order_number = ya_scooter_order_page.get_order_number()
        ya_scooter_order_page.click_go_to_status()
        current_url = ya_scooter_order_page.current_url()

        assert (Url.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)
        


