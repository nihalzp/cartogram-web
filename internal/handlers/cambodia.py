import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Cambodia"

    def get_gen_file(self):
        return "{}/cam_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 25:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Banteay Meanchey
2 {} Battambang
3 {} Kampong Cham
4 {} Kampong Chhnang
5 {} Kampong Speu
6 {} Kampong Thom
7 {} Kampot
8 {} Kandal
9 {} Koh Kong
10 {} Kep
11 {} Kratie
12 {} Pailin
13 {} Preah Sihanouk
14 {} Mondul Kiri
15 {} Otdar Meanchey
16 {} Phnom Penh
17 {} Pursat
18 {} Preah Vihear
19 {} Prey Veng
20 {} Ratanak Kiri
21 {} Siem Reap
22 {} Stung Treng
23 {} Svay Rieng
24 {} Takeo
25 {} Tbong Khmum""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Banteay Meanchey","Battambang","Kampong Cham","Kampong Chhnang","Kampong Speu","Kampong Thom","Kampot","Kandal","Koh Kong","Kep","Kratie","Pailin","Preah Sihanouk","Mondul Kiri","Otdar Meanchey","Phnom Penh","Pursat","Preah Vihear","Prey Veng","Ratanak Kiri","Siem Reap","Stung Treng","Svay Rieng","Takeo","Tbong Khmum"], [0.0 for i in range(0,25)], {"Banteay Meanchey":"1","Battambang":"2","Kampong Cham":"3","Kampong Chhnang":"4","Kampong Speu":"5","Kampong Thom":"6","Kampot":"7","Kandal":"8","Koh Kong":"9","Kep":"10","Kratie":"11","Pailin":"12","Preah Sihanouk":"13","Mondul Kiri":"14","Otdar Meanchey":"15","Phnom Penh":"16","Pursat":"17","Preah Vihear":"18","Prey Veng":"19","Ratanak Kiri":"20","Siem Reap":"21","Stung Treng":"22","Svay Rieng":"23","Takeo":"24","Tbong Khmum":"25"})
