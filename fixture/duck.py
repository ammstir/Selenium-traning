from model.duck_item import DuckItem


class DuckHelper:

    def __init__(self, app):
        self.app = app

    def get_mainpage_duck_properties(self, duck):
        duck_title = duck.find_element_by_css_selector("div.name").text
        duck_price = duck.find_element_by_css_selector("div.price-wrapper s.regular-price")
        duck_reduced_price = duck.find_element_by_css_selector("div.price-wrapper strong.campaign-price")
        duck_price_color = self.get_color(duck_price.value_of_css_property("color"))
        print("duck_price_color ", duck_price_color)
        duck_reduced_price_color = self.get_color(duck_reduced_price.value_of_css_property("color"))
        print("duck_reduced_price_color ", duck_reduced_price_color)
        duck_price_text_size = float(duck_price.value_of_css_property("font-size")[:-2])
        print("duck_price_text_size ", duck_price_text_size)
        duck_reduced_price_text_size = float(duck_reduced_price.value_of_css_property("font-size")[:-2])
        print("duck_reduced_price_text_size ", duck_reduced_price_text_size)
        duck_price_text_decoration = (duck_price.value_of_css_property("text-decoration").split(" "))[0]
        print("duck_price_text_decoration", duck_price_text_decoration)
        duck_reduced_price_font_weight = duck_reduced_price.value_of_css_property("font-weight")
        print("duck_reduced_price_font_weight ", duck_reduced_price_font_weight)
        duck_price = duck_price.text
        duck_reduced_price = duck_reduced_price.text
        return DuckItem(title=duck_title, price=duck_price, reduced_price=duck_reduced_price,
                        price_color=duck_price_color, reduced_price_color=duck_reduced_price_color,
                        price_text_size=duck_price_text_size, reduced_price_text_size=duck_reduced_price_text_size,
                        price_text_decoration=duck_price_text_decoration,
                        reduced_price_font_weight=duck_reduced_price_font_weight)

    def get_page_duck_properties(self, duck):
        duck_title = duck.find_element_by_css_selector("h1.title").text
        duck_price = duck.find_element_by_css_selector("div.price-wrapper s.regular-price")
        duck_reduced_price = duck.find_element_by_css_selector("div.price-wrapper strong.campaign-price")
        duck_price_color = self.get_color(duck_price.value_of_css_property("color"))
        duck_reduced_price_color = self.get_color(duck_reduced_price.value_of_css_property("color"))
        duck_price_text_size = float(duck_price.value_of_css_property("font-size")[:-2])
        duck_reduced_price_text_size = float(duck_reduced_price.value_of_css_property("font-size")[:-2])
        duck_price_text_decoration = (duck_price.value_of_css_property("text-decoration").split(" "))[0]
        duck_reduced_price_font_weight = duck_reduced_price.value_of_css_property("font-weight")
        duck_price = duck_price.text
        duck_reduced_price = duck_reduced_price.text
        return DuckItem(title=duck_title, price=duck_price, reduced_price=duck_reduced_price,
                        price_color=duck_price_color, reduced_price_color=duck_reduced_price_color,
                        price_text_size=duck_price_text_size, reduced_price_text_size=duck_reduced_price_text_size,
                        price_text_decoration=duck_price_text_decoration,
                        reduced_price_font_weight=duck_reduced_price_font_weight)

    def get_color(self, duck_color):
        if "rgba" in duck_color:
            color = duck_color[5:-1].split(", ")
        else:
            color = duck_color[4:-1].split(", ")
        return color
