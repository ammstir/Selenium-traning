
class DuckItem:

    def __init__(self, title=None, price=None, reduced_price=None, price_color=None, reduced_price_color=None,
                 price_text_size=None, reduced_price_text_size=None, price_text_decoration=None,
                 reduced_price_font_weight=None):
        self.title = title
        self.price = price
        self.reduced_price = reduced_price
        self.price_color = price_color
        self.reduced_price_color = reduced_price_color
        self.price_text_size = price_text_size
        self.reduced_price_text_size = reduced_price_text_size
        self.price_text_decoration = price_text_decoration
        self.reduced_price_font_weight = reduced_price_font_weight

    def __repr__(self):
        return "%s: price %d  reduced_price %d" % (self.title, self.price, self.reduced_price)
