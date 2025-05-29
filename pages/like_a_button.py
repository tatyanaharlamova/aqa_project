from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage

button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')


class LikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open Like a button page'):
            return self.browser.get("https://www.qa-practice.com/elements/button/like_a_button")

    def button(self):
        return self.find(button_selector)

    def button_click(self):
        with allure.step('Click the button'):
            self.button().click()

    def button_is_displayed(self):
        with allure.step('Check the button is displayed'):
            return self.button().is_displayed()

    def result(self):
        return self.find(result_selector)

    def result_text(self):
        with allure.step('Get result text'):
            return self.result().text

