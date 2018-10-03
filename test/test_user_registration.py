import random
import string
from selenium.webdriver.common.keys import Keys


def test_user_registration(app):
    wd = app.wd
    app.session.open_litecart()
    # генерация данных для ввода
    email = generate_email()
    password = generate_password()
    first_name = generate_name()
    last_name = generate_name()
    address = generate_address()
    city = generate_name()
    postcode = "".join([random.choice(string.digits) for i in range(5)])
    phone = "".join([random.choice(string.digits) for i in range(11)])
    # переход на страницу создания аккаунта
    wd.find_element_by_css_selector("a[href$=create_account]").click()
    # заполнение полей
    wd.find_element_by_name("firstname").send_keys(first_name)
    wd.find_element_by_name("lastname").send_keys(last_name)
    wd.find_element_by_name("address1").send_keys(address)
    wd.find_element_by_name("postcode").send_keys(postcode)
    wd.find_element_by_name("city").send_keys(city)
    wd.find_element_by_css_selector("span.selection").click()
    wd.find_element_by_css_selector("input.select2-search__field").click()
    # выбор страны
    wd.find_element_by_css_selector("input.select2-search__field").send_keys("united states" + Keys.ENTER)
    # выбор зоны
    zone = wd.find_element_by_css_selector("select[name=zone_code]")
    wd.execute_script("arguments[0].selectedIndex = 5", zone)
    # дальше заполняем поля
    wd.find_element_by_name("email").send_keys(email)
    wd.find_element_by_name("phone").send_keys(phone)
    wd.find_element_by_name("password").send_keys(password)
    wd.find_element_by_name("confirmed_password").send_keys(password)
    # создаём аккаунт
    wd.find_element_by_name("create_account").click()
    # логаутимся
    wd.find_element_by_css_selector("a[href$=logout]").click()
    # вводим данные на главной
    wd.find_element_by_name("email").send_keys(email)
    wd.find_element_by_name("password").send_keys(password)
    # логинимся
    wd.find_element_by_name("login").click()
    # логаутимся
    wd.find_element_by_css_selector("a[href$=logout]").click()


def generate_email():
    symbols = string.ascii_letters + string.digits
    email = "".join([random.choice(symbols).lower() for i in range(1, 10)]) + "@me.ru"
    return email


def generate_password():
    symbols = string.ascii_letters + string.digits
    password = "".join([random.choice(symbols) for i in range(1, 10)])
    return password


def generate_name():
    symbols = string.ascii_letters
    name = ("".join([random.choice(symbols) for i in range(5, 10)])).capitalize()
    return name


def generate_address():
    symbols = string.ascii_letters
    address = ("".join([random.choice(symbols) for i in range(10, 15)])).capitalize()
    return address
