import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Egypt"

    def get_gen_file(self):
        return "{}/egy_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 27:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """1 {} Dakahlia
2 {} Red Sea
3 {} Beheira
4 {} Fayoum
5 {} Gharbia
6 {} Alexandria
7 {} Ismailia
8 {} Giza
9 {} Monufia
10 {} Minya
11 {} Cairo
12 {} Qalyubia
13 {} Luxor
14 {} New Valley
15 {} Suez
16 {} Sharqia
17 {} Assuan
18 {} Asyut
19 {} Beni Suef
20 {} Port Said
21 {} Damietta
22 {} South Sinai
23 {} Kafr el-Sheikh
24 {} Matrouh
25 {} Qena
26 {} North Sinai
27 {} Sohag""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Governorate", 0, 1, 2, 3, ["Dakahlia","Red Sea","Beheira","Fayoum","Gharbia","Alexandria","Ismailia","Giza","Monufia","Minya","Cairo","Qalyubia","Luxor","New Valley","Suez","Sharqia","Assuan","Asyut","Beni Suef","Port Said","Damietta","South Sinai","Kafr el-Sheikh","Matrouh","Qena","North Sinai","Sohag"], [0.0 for i in range(0,27)], {"Dakahlia":"1","Red Sea":"2","Beheira":"3","Fayoum":"4","Gharbia":"5","Alexandria":"6","Ismailia":"7","Giza":"8","Monufia":"9","Minya":"10","Cairo":"11","Qalyubia":"12","Luxor":"13","New Valley":"14","Suez":"15","Sharqia":"16","Assuan":"17","Asyut":"18","Beni Suef":"19","Port Said":"20","Damietta":"21","South Sinai":"22","Kafr el-Sheikh":"23","Matrouh":"24","Qena":"25","North Sinai":"26","Sohag":"27"})
