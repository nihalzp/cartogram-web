import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Belarus"

    def get_gen_file(self):
        return "{}/belarus_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 7:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Brest
2 {} Gomel
3 {} Grodno
4 {} Mogilev
5 {} Minsk
6 {} Minsk City
7 {} Vitebsk""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Brest","Gomel","Grodno","Mogilev","Minsk","Minsk City","Vitebsk"], [0.0 for i in range(0,7)], {"Brest":"1","Gomel":"2","Grodno":"3","Mogilev":"4","Minsk":"5","Minsk City":"6","Vitebsk":"7"})
