import settings
import handlers.base_handler
import csv
class CartogramHandler(handlers.base_handler.BaseCartogramHandler):
    def get_name(self):
        return "Laos"
    def get_gen_file(self):
        return "{}/lao_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):
        if len(values) != 18:
            return False
        
        for v in values:
            if type(v) != float:
                return False
        return True
    
    def gen_area_data(self, values):
        return """1 {} Attapeu
2 {} Bokeo
3 {} Borikhamxai
4 {} Champasak
5 {} Houaphanh
6 {} Khammouane
7 {} Luang Namtha
8 {} Luang Prabang
9 {} Oudomxay
10 {} Phongsaly
11 {} Salavan
12 {} Savannakhet
13 {} Vientiane [Prefecture]
14 {} Vientiane
15 {} Xaignabouli
16 {} Xaisomboun
17 {} Sekong
18 {} Xiangkhouang""".format(*values)
    
    def expect_geojson_output(self):
        return True
    def csv_to_area_string_and_colors(self, csvfile):
        return self.order_by_example(csv.reader(csvfile), "Province", 0, 1, 2, 3, ["Attapeu","Bokeo","Borikhamxai","Champasak","Houaphanh","Khammouane","Luang Namtha","Luang Prabang","Oudomxay","Phongsaly","Salavan","Savannakhet","Vientiane [Prefecture]","Vientiane","Xaignabouli","Xaisomboun","Sekong","Xiangkhouang"], [0.0 for i in range(0,18)], {"Attapeu":"1","Bokeo":"2","Borikhamxai":"3","Champasak":"4","Houaphanh":"5","Khammouane":"6","Luang Namtha":"7","Luang Prabang":"8","Oudomxay":"9","Phongsaly":"10","Salavan":"11","Savannakhet":"12","Vientiane [Prefecture]":"13","Vientiane":"14","Xaignabouli":"15","Xaisomboun":"16","Sekong":"17","Xiangkhouang":"18"})
