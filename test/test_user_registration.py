import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from data.valid_customers import valid_customers


@pytest.mark.parametrize("customer", valid_customers, ids=[repr(x) for x in valid_customers])
def test_user_registration(app, customer):
    wd = app.wd
    app.session.open_litecart()
    # переход на страницу создания аккаунта
    wd.find_element_by_css_selector("a[href$=create_account]").click()
    # заполнение полей
    wd.find_element_by_name("firstname").send_keys(customer.firstname)
    wd.find_element_by_name("lastname").send_keys(customer.lastname)
    wd.find_element_by_name("address1").send_keys(customer.address)
    wd.find_element_by_name("postcode").send_keys(customer.postcode)
    wd.find_element_by_name("city").send_keys(customer.city)
    wd.find_element_by_css_selector("span.selection").click()
    wd.find_element_by_css_selector("input.select2-search__field").click()
    # выбор страны
    wd.find_element_by_css_selector("input.select2-search__field").send_keys(customer.country + Keys.ENTER)
    # выбор зоны
    Select(wd.find_element_by_css_selector("select[name=zone_code]")).select_by_value(customer.zone)
    # дальше заполняем поля
    wd.find_element_by_name("email").send_keys(customer.email)
    wd.find_element_by_name("phone").send_keys(app.generate.phone())
    wd.find_element_by_name("password").send_keys(customer.password)
    wd.find_element_by_name("confirmed_password").send_keys(customer.password)
    # создаём аккаунт
    wd.find_element_by_name("create_account").click()
    # логаутимся
    wd.find_element_by_css_selector("a[href$=logout]").click()
    # вводим данные на главной
    wd.find_element_by_name("email").send_keys(customer.email)
    wd.find_element_by_name("password").send_keys(customer.password)
    # логинимся
    wd.find_element_by_name("login").click()
    # логаутимся
    wd.find_element_by_css_selector("a[href$=logout]").click()


