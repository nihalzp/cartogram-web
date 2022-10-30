import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Malaysia"

    def get_gen_file(self):
        return "{}/mys_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Johor,
2,{},Kedah,
3,{},Kelantan,
4,{},Kuala Lumpur,
5,{},Labuan,
6,{},Melaka,
7,{},Negeri Sembilan,
8,{},Pahang,
9,{},Perak,
10,{},Perlis,
11,{},Pulau Pinang,
12,{},Putrajaya,
13,{},Sabah,
14,{},Sarawak,
15,{},Selangor,
16,{},Terengganu,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "State/Federal Territory", 0, 1, 2, 3, ["Johor","Kedah","Kelantan","Kuala Lumpur","Labuan","Melaka","Negeri Sembilan","Pahang","Perak","Perlis","Pulau Pinang","Putrajaya","Sabah","Sarawak","Selangor","Terengganu"], [0.0 for i in range(0,16)], {"Johor":"1","Kedah":"2","Kelantan":"3","Kuala Lumpur":"4","Labuan":"5","Melaka":"6","Negeri Sembilan":"7","Pahang":"8","Perak":"9","Perlis":"10","Pulau Pinang":"11","Putrajaya":"12","Sabah":"13","Sarawak":"14","Selangor":"15","Terengganu":"16"})
