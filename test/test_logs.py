

def test_logs(app):
    wd = app.wd
    app.session.login_to_admin()
    wd.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    ducks_list = wd.find_elements_by_css_selector('a[href*=product_id]:not([title="Edit"])')
    for i in range(len(ducks_list)):
        wd.find_element_by_css_selector('tbody tr.row:nth-child(%d) a' % (i+5)).click()
        for l in wd.get_log("browser"):
            print('Browser log: ', l)
        for l in wd.get_log("driver"):
            print('Driver log: ', l)
        wd.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
