from selenium.webdriver.common.keys import Keys


def test_user_registration(app):
    wd = app.wd
    app.session.open_litecart()
    # генерация данных для ввода
    email = app.generate.email()
    password = app.generate.password()
    # переход на страницу создания аккаунта
    wd.find_element_by_css_selector("a[href$=create_account]").click()
    # заполнение полей
    wd.find_element_by_name("firstname").send_keys(app.generate.name())
    wd.find_element_by_name("lastname").send_keys(app.generate.name())
    wd.find_element_by_name("address1").send_keys(app.generate.address())
    wd.find_element_by_name("postcode").send_keys(app.generate.postcode())
    wd.find_element_by_name("city").send_keys(app.generate.name())
    wd.find_element_by_css_selector("span.selection").click()
    wd.find_element_by_css_selector("input.select2-search__field").click()
    # выбор страны
    wd.find_element_by_css_selector("input.select2-search__field").send_keys("united states" + Keys.ENTER)
    # выбор зоны
    zone = wd.find_element_by_css_selector("select[name=zone_code]")
    wd.execute_script("arguments[0].selectedIndex = 5", zone)
    # дальше заполняем поля
    wd.find_element_by_name("email").send_keys(email)
    wd.find_element_by_name("phone").send_keys(app.generate.phone())
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


