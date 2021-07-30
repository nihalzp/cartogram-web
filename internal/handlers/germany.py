import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Germany"

    def get_gen_file(self):
        return "{}/germany_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Baden-Wuerttemberg
2 {} Bayern
3 {} Berlin
4 {} Brandenburg
5 {} Bremen
6 {} Hamburg
7 {} Hessen
8 {} Mecklenburg-Vorpommern
9 {} Niedersachsen
10 {} Nordrhein-Westfalen
11 {} Rheinland-Pfalz
12 {} Saarland
13 {} Sachsen
14 {} Sachsen-Anhalt
15 {} Schleswig-Holstein
16 {} Thueringen""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State", 0, 1, 2, 3, ["Baden-Wuerttemberg","Bayern","Berlin","Brandenburg","Bremen","Hamburg","Hessen","Mecklenburg-Vorpommern","Niedersachsen","Nordrhein-Westfalen","Rheinland-Pfalz","Saarland","Sachsen","Sachsen-Anhalt","Schleswig-Holstein","Thueringen"], [0.0 for i in range(0,16)], {"Baden-Wuerttemberg":"1","Bayern":"2","Berlin":"3","Brandenburg":"4","Bremen":"5","Hamburg":"6","Hessen":"7","Mecklenburg-Vorpommern":"8","Niedersachsen":"9","Nordrhein-Westfalen":"10","Rheinland-Pfalz":"11","Saarland":"12","Sachsen":"13","Sachsen-Anhalt":"14","Schleswig-Holstein":"15","Thueringen":"16"})
