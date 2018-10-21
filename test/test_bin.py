

def test_bin(app):
    for i in range(3):
        app.litecart.add_duck_to_bin(i)
    app.litecart.open_bin()
    for i in range(3):
        app.litecart.remove_duck_from_bin()






