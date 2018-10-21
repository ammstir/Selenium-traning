from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class LiteCartHelper:

    def __init__(self, app):
        self.app = app

    def customer_login(self, customer):
        wd = self.app.wd
        wd.find_element_by_name("email").send_keys(customer.email)
        wd.find_element_by_name("password").send_keys(customer.password)
        wd.find_element_by_name("login").click()

    def customer_logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href$=logout]").click()

    def create_new_customer(self, customer):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href$=create_account]").click()
        wd.find_element_by_name("firstname").send_keys(customer.firstname)
        wd.find_element_by_name("lastname").send_keys(customer.lastname)
        wd.find_element_by_name("address1").send_keys(customer.address)
        wd.find_element_by_name("postcode").send_keys(customer.postcode)
        wd.find_element_by_name("city").send_keys(customer.city)
        self.select_country(customer)
        self.select_zone(customer)
        wd.find_element_by_name("email").send_keys(customer.email)
        wd.find_element_by_name("phone").send_keys(customer.phone)
        wd.find_element_by_name("password").send_keys(customer.password)
        wd.find_element_by_name("confirmed_password").send_keys(customer.password)
        wd.find_element_by_name("create_account").click()

    def select_zone(self, customer):
        wd = self.app.wd
        Select(wd.find_element_by_css_selector("select[name=zone_code]")).select_by_value(customer.zone)

    def select_country(self, customer):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.selection").click()
        wd.find_element_by_css_selector("input.select2-search__field").click()
        wd.find_element_by_css_selector("input.select2-search__field").send_keys(customer.country + Keys.ENTER)
