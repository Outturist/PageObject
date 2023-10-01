from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_page_url = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        actual_url = self.browser.current_url
        assert login_page_url == actual_url, f'Ожидаемый адрес страницы:{login_page_url} Факический адрес страницы:{actual_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма логина на странице логина/аторизации отсутствует'


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации на странице логина/аторизации отсутствует'
