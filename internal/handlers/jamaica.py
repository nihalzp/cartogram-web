import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Jamaica"

    def get_gen_file(self):
        return "{}/jamaica_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 14:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Clarendon,
2,{},Hanover,
3,{},Kingston,
4,{},Manchester,
5,{},Portland,
6,{},Saint Andrew,
7,{},Saint Ann,
8,{},Saint Catherine,
9,{},Saint Elizabeth,
10,{},Saint James,
11,{},Saint Mary,
12,{},Saint Thomas,
13,{},Trelawny,
14,{},Westmoreland,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Parish", 0, 1, 2, 3, ["Clarendon","Hanover","Kingston","Manchester","Portland","Saint Andrew","Saint Ann","Saint Catherine","Saint Elizabeth","Saint James","Saint Mary","Saint Thomas","Trelawny","Westmoreland"], [0.0 for i in range(0,14)], {"Clarendon":"1","Hanover":"2","Kingston":"3","Manchester":"4","Portland":"5","Saint Andrew":"6","Saint Ann":"7","Saint Catherine":"8","Saint Elizabeth":"9","Saint James":"10","Saint Mary":"11","Saint Thomas":"12","Trelawny":"13","Westmoreland":"14"})
