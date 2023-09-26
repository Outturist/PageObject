from time import sleep

LINK = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestMainPage:
    def test_open_main_page(self, browser):
        browser.get(LINK)
        browser.maximize_window()
        sleep(3)