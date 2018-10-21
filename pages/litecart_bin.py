from selenium.webdriver.support.wait import WebDriverWait


class LiteCartBin:

    def __init__(self, app):
        self.app = app

    def wait_row_count_decrease(self, rows_count):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(lambda x: len(wd.find_elements_by_css_selector("td.item")) == (rows_count - 1))

    def remove_item(self):
        wd = self.app.wd
        wd.find_element_by_name("remove_cart_item").click()

    def items_rows_count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("td.item"))