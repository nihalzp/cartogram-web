import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Qatar"

    def get_gen_file(self):
        return "{}/qat_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 8:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Al Daayen,
2,{},Al Khor,
3,{},Al Rayyan,
4,{},Al Shamal,
5,{},Al Wakrah,
6,{},Al-Shahaniya,
7,{},Doha,
8,{},Umm Salal,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Municipality", 0, 1, 2, 3, ["Al Daayen","Al Khor","Al Rayyan","Al Shamal","Al Wakrah","Al-Shahaniya","Doha","Umm Salal"], [0.0 for i in range(0,8)], {"Al Daayen":"1","Al Khor":"2","Al Rayyan":"3","Al Shamal":"4","Al Wakrah":"5","Al-Shahaniya":"6","Doha":"7","Umm Salal":"8"})
