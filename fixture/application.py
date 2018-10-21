from selenium import webdriver
from fixture.session import SessionHelper
from fixture.admin import Admin
from fixture.duck import DuckHelper
from fixture.litecart import LiteCartHelper


class Application:

    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.duck = DuckHelper(self)
        self.admin = Admin(self)
        self.litecart = LiteCartHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
