import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "San Marino"

    def get_gen_file(self):
        return "{}/smr_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 9:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Acquaviva,
2,{},Borgo Maggiore,
3,{},Chiesanuova,
4,{},Domagnano,
5,{},Faetano,
6,{},Fiorentino,
7,{},Montegiardino,
8,{},San Marino,
9,{},Serravalle,""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Municipality", 0, 1, 2, 3, ["Acquaviva","Borgo Maggiore","Chiesanuova","Domagnano","Faetano","Fiorentino","Montegiardino","San Marino","Serravalle"], [0.0 for i in range(0,9)], {"Acquaviva":"1","Borgo Maggiore":"2","Chiesanuova":"3","Domagnano":"4","Faetano":"5","Fiorentino":"6","Montegiardino":"7","San Marino":"8","Serravalle":"9"})
