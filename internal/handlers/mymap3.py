import settings
import handlers.base_handler
import csv
import types

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "My Map 3"

    def get_gen_file(self):
        return "{}/addmap_data/mymap3/mymap3_processed.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 3:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Bruxelles,
2,{},Vlaanderen,
3,{},Wallonie,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):
        if(isinstance(csvfile, types.GeneratorType)):
            csvfile = csv.reader(csvfile)
        return self.order_by_example(csvfile, "State", 0, 1, 2, 3, ["Bruxelles","Vlaanderen","Wallonie"], [0.0 for i in range(0,3)], {"Bruxelles":"1","Vlaanderen":"2","Wallonie":"3"})
