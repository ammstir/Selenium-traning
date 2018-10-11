import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_new_windows_opening(app):
    wd = app.wd
    wait = WebDriverWait(wd, 10)
    new_window_id = ""
    app.admin.open_countries()
    countries = wd.find_elements_by_css_selector("a[href*=country_code][title=Edit]")
    country = random.choice(countries)
    country.click()
    base_window_id = wd.current_window_handle
    old_windows_list = wd.window_handles
    links = wd.find_elements_by_css_selector("a[target=_blank]")[4:]
    for link in links:
        link.click()
        wait.until(EC.new_window_is_opened(old_windows_list))
        new_windows_list = wd.window_handles
        for id in new_windows_list:
            if id not in old_windows_list:
                new_window_id = id
                break
        wd.switch_to_window(new_window_id)
        wd.close()
        wd.switch_to_window(base_window_id)
