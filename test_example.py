import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(capabilities={"marionette": False})
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://yandex.ru")
    driver.find_element_by_name("text").send_keys("webdriver")
