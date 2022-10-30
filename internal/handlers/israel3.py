import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Israel"

    def get_gen_file(self):
        return "{}/isr3_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 6:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},HaDarom,
2,{},Haifa,
3,{},HaMerkaz,
4,{},HaZafon,
5,{},Jerusalem,
6,{},Tel Aviv,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "District", 0, 1, 2, 3, ["HaDarom","Haifa","HaMerkaz","HaZafon","Jerusalem","Tel Aviv"], [0.0 for i in range(0,6)], {"HaDarom":"1","Haifa":"2","HaMerkaz":"3","HaZafon":"4","Jerusalem":"5","Tel Aviv":"6"})
