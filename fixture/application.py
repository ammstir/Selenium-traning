from selenium import webdriver
from fixture.session import SessionHelper
from fixture.admin import Admin


class Application:
    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.admin = Admin(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
