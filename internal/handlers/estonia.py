import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Estonia"

    def get_gen_file(self):
        return "{}/est_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 15:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Harju
2 {} Hiiu
3 {} Ida-Viru
4 {} Jarva
5 {} Jogeva
6 {} Laane
7 {} Laane-Viru
8 {} Parnu
9 {} Polva
10 {} Rapla
11 {} Saare
12 {} Tartu
13 {} Valga
14 {} Vilijandi
15 {} Voru""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "County", 0, 1, 2, 3, ["Harju","Hiiu","Ida-Viru","Jarva","Jogeva","Laane","Laane-Viru","Parnu","Polva","Rapla","Saare","Tartu","Valga","Vilijandi","Voru"], [0.0 for i in range(0,15)], {"Harju":"1","Hiiu":"2","Ida-Viru":"3","Jarva":"4","Jogeva":"5","Laane":"6","Laane-Viru":"7","Parnu":"8","Polva":"9","Rapla":"10","Saare":"11","Tartu":"12","Valga":"13","Vilijandi":"14","Voru":"15"})
