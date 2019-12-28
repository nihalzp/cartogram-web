import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "CZE Unicode"

    def get_gen_file(self):
        return "{}/cze_processedmap_(1).json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 14:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Jihomoravský
2 {} Jihočeský
3 {} Karlovarský
4 {} Kraj Vysočina
5 {} Královéhradecký
6 {} Liberecký
7 {} Moravskoslezský
8 {} Olomoucký
9 {} Pardubický
10 {} Plzeňský
11 {} Prague
12 {} Středočeský
13 {} Zlínský
14 {} Ústecký""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Jihomoravský","Jihočeský","Karlovarský","Kraj Vysočina","Královéhradecký","Liberecký","Moravskoslezský","Olomoucký","Pardubický","Plzeňský","Prague","Středočeský","Zlínský","Ústecký"], [0.0 for i in range(0,14)], {"Jihomoravský":"1","Jihočeský":"2","Karlovarský":"3","Kraj Vysočina":"4","Královéhradecký":"5","Liberecký":"6","Moravskoslezský":"7","Olomoucký":"8","Pardubický":"9","Plzeňský":"10","Prague":"11","Středočeský":"12","Zlínský":"13","Ústecký":"14"})
