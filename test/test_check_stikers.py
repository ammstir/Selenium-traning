
def test_check_stickers(app):
    wd = app.wd
    app.session.open_litecart()
    ducks = wd.find_elements_by_css_selector("li.product a.link[title$=Duck]")
    for duck in ducks:
        stickers = duck.find_elements_by_css_selector("div.sticker")
        assert len(stickers) == 1
