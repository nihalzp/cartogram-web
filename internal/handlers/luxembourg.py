import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Luxembourg"

    def get_gen_file(self):
        return "{}/lux_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 12:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Capellen
2 {} Clervaux
3 {} Diekirch
4 {} Echternach
5 {} Esch-sur-Alzette
6 {} Grevenmacher
7 {} Luxembourg
8 {} Mersch
9 {} Redange
10 {} Remich
11 {} Vianden
12 {} Wiltz""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Canton", 0, 1, 2, 3, ["Capellen","Clervaux","Diekirch","Echternach","Esch-sur-Alzette","Grevenmacher","Luxembourg","Mersch","Redange","Remich","Vianden","Wiltz"], [0.0 for i in range(0,12)], {"Capellen":"1","Clervaux":"2","Diekirch":"3","Echternach":"4","Esch-sur-Alzette":"5","Grevenmacher":"6","Luxembourg":"7","Mersch":"8","Redange":"9","Remich":"10","Vianden":"11","Wiltz":"12"})
