import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "New Zealand"

    def get_gen_file(self):
        return "{}/newZealand_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 16:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Auckland,
2,{},Bay of Plenty,
3,{},Canterbury,
4,{},Gisborne,
5,{},Hawke's Bay,
6,{},Manawatu-Wanganui,
7,{},Marlborough,
8,{},Nelson,
9,{},Northland,
10,{},Otago,
11,{},Southland,
12,{},Taranaki,
13,{},Tasman,
14,{},Waikato,
15,{},Wellington,
16,{},West Coast,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Auckland","Bay of Plenty","Canterbury","Gisborne","Hawke's Bay","Manawatu-Wanganui","Marlborough","Nelson","Northland","Otago","Southland","Taranaki","Tasman","Waikato","Wellington","West Coast"], [0.0 for i in range(0,16)], {"Auckland":"1","Bay of Plenty":"2","Canterbury":"3","Gisborne":"4","Hawke's Bay":"5","Manawatu-Wanganui":"6","Marlborough":"7","Nelson":"8","Northland":"9","Otago":"10","Southland":"11","Taranaki":"12","Tasman":"13","Waikato":"14","Wellington":"15","West Coast":"16"})
