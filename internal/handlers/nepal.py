import settings
import handlers.base_handler
import csv
class CartogramHandler(handlers.base_handler.BaseCartogramHandler):
    def get_name(self):
        return "Nepal"
    def get_gen_file(self):
        return "{}/nepal_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):
        if len(values) != 7:
            return False
        
        for v in values:
            if type(v) != float:
                return False
        return True
    
    def gen_area_data(self, values):
        return """1 {} Bagmati Pradesh
2 {} Gandaki Pradesh
3 {} Karnali Pradesh
4 {} Province No. 1
5 {} Province No. 2
6 {} Province No. 5
7 {} Sudurpashchim Pradesh""".format(*values)
    
    def expect_geojson_output(self):
        return True
    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Bagmati Pradesh","Gandaki Pradesh","Karnali Pradesh","Province No. 1","Province No. 2","Province No. 5","Sudurpashchim Pradesh"], [0.0 for i in range(0,7)], {"Bagmati Pradesh":"1","Gandaki Pradesh":"2","Karnali Pradesh":"3","Province No. 1":"4","Province No. 2":"5","Province No. 5":"6","Sudurpashchim Pradesh":"7"})
