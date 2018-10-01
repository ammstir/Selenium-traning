
def test_check_countries_order(app):
    wd = app.wd
    app.session.login_to_admin()
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    table = wd.find_element_by_css_selector("table.dataTable")
    country_list = app.admin.get_countries_list(table)
    assert country_list == sorted(country_list)
    # ниже говно
    rows = table.find_elements_by_css_selector("tr.row")
    for row in rows:
        if int(row.find_elements_by_tag_name("td")[5].text) > 0:
            row.find_element_by_css_selector("[href*=country_code]:([title='Edit'])").click()
            table = wd.find_element_by_css_selector("table.dataTable")
            country_list = app.admin.get_countries_list(table)
            assert country_list == sorted(country_list)
            wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
