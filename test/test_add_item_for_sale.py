import random
import os.path


def test_add_item_for_sale(app):
    wd = app.wd
    app.session.login_to_admin()
    wd.implicitly_wait(5)
    item_name = app.generate.name()
    wd.find_element_by_css_selector("a[href$=catalog]").click()
    wd.find_element_by_css_selector("a[href$=edit_product]").click()
    # заполняем первую страницу
    wd.find_elements_by_css_selector("[type=radio]")[0].click()
    wd.find_element_by_name("name[en]").send_keys(item_name)
    wd.find_element_by_name("code").send_keys(app.generate.itemcode())
    categories_checkboxes = wd.find_elements_by_name("categories[]")
    for checkbox in categories_checkboxes:
        app.admin.check_checkbox(checkbox)
    wd.execute_script("arguments[0].selectedIndex = 1", wd.find_element_by_name("default_category_id"))
    gender_checkboxes = wd.find_elements_by_name("product_groups[]")
    for checkbox in gender_checkboxes:
        app.admin.check_checkbox(checkbox)
    wd.find_element_by_name("quantity").clear()
    wd.find_element_by_name("quantity").send_keys(random.choice(range(50)))
    wd.execute_script("arguments[0].selectedIndex = 1", wd.find_element_by_name("quantity"))
    wd.execute_script("arguments[0].selectedIndex = 1", wd.find_element_by_name("delivery_status_id"))
    wd.execute_script("arguments[0].selectedIndex = 1", wd.find_element_by_name("sold_out_status_id"))
    wd.find_element_by_name("new_images[]").send_keys(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data/cat.jpg"))
    wd.find_element_by_name("date_valid_from").send_keys("2018-02-02")
    wd.find_element_by_name("date_valid_to").send_keys("2020-02-02")
    # заполняем вторую страницу
    wd.find_element_by_css_selector("a[href=\#tab-information]").click()
    wd.execute_script("arguments[0].selectedIndex = 1", wd.find_element_by_name("manufacturer_id"))
    wd.find_element_by_name("keywords").send_keys(app.generate.name()+", cat")
    wd.find_element_by_name("short_description[en]").send_keys(app.generate.random_string(20))
    wd.find_element_by_css_selector("div.trumbowyg-editor").send_keys(app.generate.random_string(50))
    wd.find_element_by_name("head_title[en]").send_keys(app.generate.random_string(10))
    wd.find_element_by_name("meta_description[en]").send_keys(app.generate.random_string(10))
    # заполняем третью страницу
    wd.find_element_by_css_selector("a[href=\#tab-prices]").click()
    wd.find_element_by_name("purchase_price").clear()
    wd.find_element_by_name("purchase_price").send_keys(app.generate.random_numbers(20))
    wd.execute_script("arguments[0].selectedIndex = 2", wd.find_element_by_name("purchase_price_currency_code"))
    wd.find_element_by_name("prices[USD]").send_keys(app.generate.random_numbers(50))
    wd.find_element_by_name("prices[EUR]").send_keys(app.generate.random_numbers(50))
    # сохраняем
    wd.find_element_by_name("save").click()
    # проверяем наличие в каталоге
    assert app.session.check_exists_by_link_text(item_name)
