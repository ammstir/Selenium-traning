from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_bin(app):
    wd = app.wd
    wait = WebDriverWait(wd, 10)
    i = 0
    while True:
        app.session.open_litecart()
        quantity = wd.find_element_by_css_selector("span.quantity").text
        wd.find_element_by_css_selector("ul.listing-wrapper.products li.product:nth-child(%d)" % (i+1)).click()
        if app.session.check_exists_by_css("select[name*=options]"):
            wd.execute_script("arguments[0].selectedIndex = 2", wd.find_element_by_css_selector("select[name*=options]"))
        wd.find_element_by_name("add_cart_product").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), "%d" % (int(quantity)+1)))
        if wd.find_element_by_css_selector("span.quantity").text == "3":
            break
    wd.find_element_by_link_text("Checkout »").click()
    wd.find_element_by_css_selector("li.shortcut").click()
    for i in range(3):
        rows_count = len(wd.find_elements_by_css_selector("td.item"))
        wd.find_element_by_name("remove_cart_item").click()
        wait.until(lambda x: len(wd.find_elements_by_css_selector("td.item")) == (rows_count-1))
