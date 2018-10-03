
def test_check_product_page(app):
    wd = app.wd
    app.session.open_litecart()
    duck_mainpage = wd.find_element_by_css_selector("div#box-campaigns li.product a.link[title$=Duck]")
    duck_from_mainpage = app.duck.get_mainpage_duck_properties(duck_mainpage)
    assert duck_from_mainpage.price_text_decoration == "line-through"
    assert (duck_from_mainpage.price_color[0] == duck_from_mainpage.price_color[1] and
           duck_from_mainpage.price_color[1] == duck_from_mainpage.price_color[2])
    assert duck_from_mainpage.reduced_price_color[1] == "0" and duck_from_mainpage.reduced_price_color[2] == "0"
    assert duck_from_mainpage.reduced_price_font_weight == "bold" or int(duck_from_mainpage.reduced_price_font_weight) >= 700
    assert duck_from_mainpage.price_text_size < duck_from_mainpage.reduced_price_text_size
    duck_mainpage.click()
    duck_page = wd.find_element_by_css_selector("div#box-product")
    duck_from_page = app.duck.get_page_duck_properties(duck_page)
    assert duck_from_page.price_text_decoration == "line-through"
    assert (duck_from_page.price_color[0] == duck_from_page.price_color[1] and
            duck_from_page.price_color[1] == duck_from_page.price_color[2])
    assert duck_from_page.reduced_price_color[1] == "0" and duck_from_page.reduced_price_color[2] == "0"
    assert duck_from_page.reduced_price_font_weight == "bold" or int(duck_from_page.reduced_price_font_weight) >= 700
    assert duck_from_page.price_text_size < duck_from_page.reduced_price_text_size

    assert duck_from_mainpage.title == duck_from_page.title
    assert duck_from_mainpage.price == duck_from_page.price
    assert duck_from_mainpage.reduced_price == duck_from_page.reduced_price
