
def test_go_through_sidebar(app):
    wd = app.wd
    # wd.implicitly_wait(5)
    app.session.login_to_admin()
    menu = wd.find_elements_by_css_selector("ul#box-apps-menu li#app-")
    count = len(list(menu))
    for i in range(count):
        wd.find_element_by_css_selector("ul#box-apps-menu li#app-:nth-child(%d)" % (i+1)).click()
        assert app.session.check_exists_by_css("h1")
        if app.session.check_exists_by_css("ul.docs"):
            count = len(list(wd.find_elements_by_css_selector("ul.docs li")))
            for j in range(count):
                wd.find_element_by_css_selector("ul.docs li:nth-child(%d)" % (j + 1)).click()
                assert app.session.check_exists_by_css("h1")
