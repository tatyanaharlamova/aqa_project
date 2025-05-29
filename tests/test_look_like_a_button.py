from pages.like_a_button import LikeAButtonPage
import allure


@allure.feature('Like a button')
@allure.story('existence')
def test_button2_exist(browser):
    like_a_button = LikeAButtonPage(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed()


@allure.feature('Like a button')
@allure.story('clickability')
def test_button2_clicked(browser):
    like_a_button = LikeAButtonPage(browser)
    like_a_button.open()
    like_a_button.button_click()
    with allure.step('Check result'):
        assert 'Submitted' == like_a_button.result_text()
