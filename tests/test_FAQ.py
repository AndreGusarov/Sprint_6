import pytest
import allure

from pages.home_page import YaScooterHomePage
from data.test_data import YaScooterHomePageFAQ
from data.locators import YaScooterHomePageLocator
from selenium.webdriver.support import expected_conditions as EC  

@allure.epic('Main page')
@allure.parent_suite('FAQ tests')
@allure.suite('FAQ suite')
class TestYaScooterFAQPage:
    @allure.feature('Аккордеон')
    @allure.story('При нажатии на вопрос в разделе FAQ пользователь должен получить ответ')
    @allure.title('При нажатии на вопрос появляется ответ')
    @allure.description('Проверка, что при нажатии на порос в разделе FAQ, выпадает ответ и текст ответа соответствет требованиям ')

    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookies_accept()
        ya_scooter_home_page.scroll_page()
        ya_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.FAQ_ANSWER(answer_number=answer))
      
        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ не совпадает с требованиями'
    