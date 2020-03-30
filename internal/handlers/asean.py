import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "ASEAN Countries"

    def get_gen_file(self):
        return "{}/asean_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 10:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} BRN
2 {} IDN
3 {} KHM
4 {} LAO
5 {} MMR
6 {} MYS
7 {} PHL
8 {} SGP
9 {} THA
10 {} VNM""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Country", 0, 1, 2, 3, ["BRN","IDN","KHM","LAO","MMR","MYS","PHL","SGP","THA","VNM"], [0.0 for i in range(0,10)], {"BRN":"1","IDN":"2","KHM":"3","LAO":"4","MMR":"5","MYS":"6","PHL":"7","SGP":"8","THA":"9","VNM":"10"})
