from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LiteCartHomePage:

    def __init__(self, app):
        self.app = app

    def wait_counter_increase(self, quantity):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), "%d" % (int(quantity) + 1)))

    def click_add_to_bin(self):
        wd = self.app.wd
        self.select_duck_size()
        wd.find_element_by_name("add_cart_product").click()

    def select_duck_size(self):
        wd = self.app.wd
        if self.app.session.check_exists_by_css("select[name*=options]"):
            wd.execute_script("arguments[0].selectedIndex = 2", wd.find_element_by_css_selector("select[name*=options]"))

    def choose_duck_on_homepage(self, i):
        wd = self.app.wd
        wd.find_element_by_css_selector("ul.listing-wrapper.products li.product:nth-child(%d)" % (i + 1)).click()

    def check_duck_quantity(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.quantity").text



