

class Admin:

    def __init__(self, app):
        self.app = app

    def get_countries_list(self):
        wd = self.app.wd
        country_list = []
        rows = wd.find_elements_by_css_selector("table.dataTable tr.row")
        for row in rows:
            country_list.append(row.find_element_by_css_selector("a[href*=country_code]:not([title=Edit])").text)
        return country_list

    def get_geo_zones_list(self):
        wd = self.app.wd
        zones_list = []
        rows = wd.find_elements_by_css_selector("table.dataTable tr.row")
        for row in rows:
            zones_list.append(row.find_element_by_css_selector("a[href*=edit_geo_zone]:not([title=Edit])").text)
        return zones_list
