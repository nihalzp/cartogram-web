import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Pakistan"

    def get_gen_file(self):
        return "{}/pak_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 8:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Azad Kashmir,
2,{},Balochistan,
3,{},Federally Administered Tribal Areas,
4,{},Gilgit-Baltistan,
5,{},Islamabad Capital Territory,
6,{},Khyber Pakhtunkhwa,
7,{},Punjab,
8,{},Sindh,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Division", 0, 1, 2, 3, ["Azad Kashmir","Balochistan","Federally Administered Tribal Areas","Gilgit-Baltistan","Islamabad Capital Territory","Khyber Pakhtunkhwa","Punjab","Sindh"], [0.0 for i in range(0,8)], {"Azad Kashmir":"1","Balochistan":"2","Federally Administered Tribal Areas":"3","Gilgit-Baltistan":"4","Islamabad Capital Territory":"5","Khyber Pakhtunkhwa":"6","Punjab":"7","Sindh":"8"})
