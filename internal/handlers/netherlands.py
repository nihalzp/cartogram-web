import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Netherlands"

    def get_gen_file(self):
        return "{}/netherlands_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 12:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Drenthe,
2,{},Flevoland,
3,{},Friesland,
4,{},Gelderland,
5,{},Groningen,
6,{},Limburg,
7,{},Noord-Brabant,
8,{},Noord-Holland,
9,{},Overijssel,
10,{},Utrecht,
11,{},Zeeland,
12,{},Zuid-Holland,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Drenthe","Flevoland","Friesland","Gelderland","Groningen","Limburg","Noord-Brabant","Noord-Holland","Overijssel","Utrecht","Zeeland","Zuid-Holland"], [0.0 for i in range(0,12)], {"Drenthe":"1","Flevoland":"2","Friesland":"3","Gelderland":"4","Groningen":"5","Limburg":"6","Noord-Brabant":"7","Noord-Holland":"8","Overijssel":"9","Utrecht":"10","Zeeland":"11","Zuid-Holland":"12"})
