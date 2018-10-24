from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


def test_check_stickers(app):
    wd = EventFiringWebDriver(app.wd, MyListener())
    app.session.open_litecart_homepage()
    ducks = wd.find_elements_by_css_selector("li.product")
    for duck in ducks:
        stickers = duck.find_elements_by_css_selector("div.sticker")
        assert len(stickers) == 1

