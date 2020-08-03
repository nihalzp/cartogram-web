import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Angola"

    def get_gen_file(self):
        return "{}/angola_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Bengo
2 {} Benguela
3 {} Bie
4 {} Cabinda
5 {} Cuando Cubango
6 {} Cuanza Norte
7 {} Cuanza Sul
8 {} Cunene
9 {} Huambo
10 {} Huila
11 {} Luanda
12 {} Lunda Norte
13 {} Lunda Sul
14 {} Malanje
15 {} Moxico
16 {} Namibe
17 {} Uige
18 {} Zaire""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Bengo","Benguela","Bie","Cabinda","Cuando Cubango","Cuanza Norte","Cuanza Sul","Cunene","Huambo","Huila","Luanda","Lunda Norte","Lunda Sul","Malanje","Moxico","Namibe","Uige","Zaire"], [0.0 for i in range(0,18)], {"Bengo":"1","Benguela":"2","Bie":"3","Cabinda":"4","Cuando Cubango":"5","Cuanza Norte":"6","Cuanza Sul":"7","Cunene":"8","Huambo":"9","Huila":"10","Luanda":"11","Lunda Norte":"12","Lunda Sul":"13","Malanje":"14","Moxico":"15","Namibe":"16","Uige":"17","Zaire":"18"})
