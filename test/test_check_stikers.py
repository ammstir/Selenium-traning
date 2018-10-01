
def test_check_stickers(app):
    wd = app.wd
    app.session.open_litecart()
    ducks = wd.find_elements_by_css_selector("div.image-wrapper")
    stickers = wd.find_elements_by_css_selector("div.sticker")
    assert len(list(ducks)) == len(list(stickers))
