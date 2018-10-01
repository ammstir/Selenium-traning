

class Admin:

    def __init__(self, app):
        self.app = app

    def get_countries_list(self, table):
        country_list = []
        rows = table.find_elements_by_css_selector("tr.row")
        for row in rows:
            country_list.append(row.find_element_by_tag_name("[href*=country_code]:not([title='Edit'])").text)
        return country_list
