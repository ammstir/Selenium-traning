from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_to_admin(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/admin/")
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()

    def open_litecart(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/en/")

    def check_exists_by_css(self, css):
        wd = self.app.wd
        try:
            wd.find_element_by_css_selector(css)
            return True
        except NoSuchElementException:
            return False

    def check_exists_by_link_text(self, text):
        wd = self.app.wd
        try:
            wd.find_element_by_link_text(text)
            return True
        except NoSuchElementException:
            return False
