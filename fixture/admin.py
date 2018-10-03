

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

    def get_subcountry_list(self):
        subcountry_list = []
        subcountry_list_rows = wd.find_elements_by_css_selector("table#table-zones tr:not([class=header])")[:-1]
        for sub_row in subcountry_list_rows:
            subcountry_list.append(
                sub_row.find_element_by_css_selector("input[name$=\\]\\[name\\]]").get_attribute("value"))
        return subcountry_list

    def get_geo_zones_list(self):
        wd = self.app.wd
        zones_list = []
        rows = wd.find_elements_by_css_selector("table.dataTable tr.row")
        for row in rows:
            zones_list.append(row.find_element_by_css_selector("td:nth-child(4)").text)
        return zones_list
