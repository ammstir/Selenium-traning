
def test_check_stickers(app):
    wd = app.wd
    app.session.open_litecart()
    ducks = wd.find_elements_by_css_selector("li.product.column.shadow.hover-light")
    for duck in ducks:
        stickers = duck.find_elements_by_css_selector("a.link[title$=Duck] div.sticker")
        assert len(stickers) <= 1
