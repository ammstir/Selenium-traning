
def test_check_countries_order_countries(app):
    wd = app.wd
    app.session.login_to_admin()
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    country_list = app.admin.get_countries_list()
    assert country_list == sorted(country_list)
    rows_count = len(wd.find_elements_by_css_selector("table.dataTable tr.row"))
    for i in range(rows_count):
        row = wd.find_element_by_css_selector("table.dataTable tbody tr.row:nth-child(%d)" % (i+2))
        zones = row.find_element_by_css_selector("td:nth-child(6)").text
        if int(zones) > 0:
            row.find_element_by_css_selector("a[href*=country_code]:not([title=Edit])").click()
            subcountry_list = app.admin.get_subcountry_list()
            assert subcountry_list == sorted(subcountry_list)
            wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")


def test_check_countries_order_geo_zones(app):
    wd = app.wd
    app.session.login_to_admin()
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    zones_list = app.admin.get_geo_zones_list()
    assert zones_list == sorted(zones_list)
