import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Pakistan"

    def get_gen_file(self):
        return "{}/pak_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 7:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Azad Kashmir
2 {} Balochistan
3 {} Islamabad Capital Territory
4 {} Khyber Pakhtunkhwa
5 {} Gilgit-Baltistan
6 {} Punjab
7 {} Sindh""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Azad Kashmir","Balochistan","Islamabad Capital Territory","Khyber Pakhtunkhwa","Gilgit-Baltistan","Punjab","Sindh"], [0.0 for i in range(0,7)], {"Azad Kashmir":"1","Balochistan":"2","Islamabad Capital Territory":"3","Khyber Pakhtunkhwa":"4","Gilgit-Baltistan":"5","Punjab":"6","Sindh":"7"})
