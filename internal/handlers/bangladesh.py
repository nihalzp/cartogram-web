import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Bangladesh"

    def get_gen_file(self):
        return "{}/bangladesh_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 8:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Barisal,
2,{},Chittagong,
3,{},Dhaka,
4,{},Khulna,
5,{},Mymensingh,
6,{},Rajshahi,
7,{},Rangpur,
8,{},Sylhet,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Division", 0, 1, 2, 3, ["Barisal","Chittagong","Dhaka","Khulna","Mymensingh","Rajshahi","Rangpur","Sylhet"], [0.0 for i in range(0,8)], {"Barisal":"1","Chittagong":"2","Dhaka":"3","Khulna":"4","Mymensingh":"5","Rajshahi":"6","Rangpur":"7","Sylhet":"8"})
