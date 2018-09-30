import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Chrome()
    # wd = webdriver.Safari()
    request.addfinalizer(wd.quit)
    return wd

#
# def test_go_through_sidebar(driver):
#     driver.get("http://localhost/litecart/admin/")
#     driver.find_element_by_name("username").send_keys("admin")
#     driver.find_element_by_name("password").send_keys("admin")
#     driver.find_element_by_name("login").click()
#     driver.implicitly_wait(20)
#     menu = driver.find_element_by_css_selector("ul#box-apps-menu")
#     link_in_menu = list(menu.find_elements_by_tag_name("a"))
#     for link in link_in_menu:
#         link.click()


def test_check_stickers(driver):
    driver.get("http://localhost/litecart/en/")
    driver.implicitly_wait(10)
    ducks = driver.find_elements_by_css_selector("div.image-wrapper")
    stickers = driver.find_elements_by_css_selector("div.sticker")
    assert len(list(ducks)) == len(list(stickers))

