import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Andorra"

    def get_gen_file(self):
        return "{}/and_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 7:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Andorra la Vella,
2,{},Canillo,
3,{},Encamp,
4,{},Escaldes-Engordany,
5,{},La Massana,
6,{},Ordino,
7,{},Sant Julia de Loria,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Parish", 0, 1, 2, 3, ["Andorra la Vella","Canillo","Encamp","Escaldes-Engordany","La Massana","Ordino","Sant Julia de Loria"], [0.0 for i in range(0,7)], {"Andorra la Vella":"1","Canillo":"2","Encamp":"3","Escaldes-Engordany":"4","La Massana":"5","Ordino":"6","Sant Julia de Loria":"7"})
